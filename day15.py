import os

from aoc_tools import get_data
from intcode_computer import IntcodeComputer

dirs = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
dirs_set = {1, 2, 3, 4}
inverse_directions = {1: 2, 2: 1, 3: 4, 4: 3}

debug_mode_bfs = True
debug_mode_graph = True
debug_mode_queue = False
debug_mode_bot = True


def all_directions_covered(direction_covered):
    return all([len(x) == 4 for x in direction_covered.values()])


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)
    computer.compute_while_possible()

    bot = Bot(computer)
    return bot.run()


def part2(data: str):
    pass


def is_covered(position, graph):
    return position in graph and len(graph[position]) == 4


class Bot:
    def __init__(self, computer: IntcodeComputer):
        self.maze = Maze()
        self.computer = computer
        self.position = (0, 0)

    def run(self):

        while True:
            exploration_position, path = self.find_position_to_explore()
            if path is None:
                print("End of exploration")
                break
            self.travel_to_position(path)
            self.explore()

        bfs = BFS(self.maze, self.maze.finish)
        p, path = bfs.search(lambda pos, graph: pos == (0, 0))
        print("Result path to {}: {}".format(p, path))
        return len(path) - 1

    def find_position_to_explore(self):
        bfs = BFS(self.maze, self.position)
        return bfs.search(lambda pos, graph: not is_covered(pos, graph))

    def travel_to_position(self, path):
        if debug_mode_bot:
            print("Bot: traveling using path {}".format(path))
        for p in path[1:]:
            self.computer.accept_input([p])
            self.computer.compute_while_possible()
            if debug_mode_bot:
                print("Bot: input: {} output: {}".format(p, self.computer.output))
            self.computer.reset_output()

            direction = dirs[p]
            self.position = add_2d(self.position, direction)
            if debug_mode_bot:
                print("Bot: new position {}".format(self.position))

    def explore(self):
        direction_idx, target = self.maze.give_unknown_direction(self.position)

        self.computer.accept_input([direction_idx])
        self.computer.compute_while_possible()
        codes = self.computer.output
        self.computer.reset_output()

        if debug_mode_bot:
            print("Exploring {} direction {}, output {}".format(self.position, direction_idx, codes))

        self.maze.add_connection(self.position, direction_idx)

        first_code = codes[0]
        if first_code == 0:
            # no move
            self.maze.set_wall(target)
            return

        self.position = target
        if debug_mode_bot:
            print("Bot: moved to {}".format(self.position))

            if first_code == 2:
                self.maze.set_finish(target)


class Maze:

    def __init__(self):
        self.graph = {(0, 0): set()}
        self.walls = set()
        self.start = (0, 0)
        self.finish = None

    def give_unknown_direction(self, position):
        known = self.graph[position]
        for dir_idx in dirs:
            direction = dirs[dir_idx]
            target = add_2d(direction, position)
            if target not in known:
                return dir_idx, target

        return None

    def add_connection(self, position, dir_idx):
        direction = dirs[dir_idx]
        target = add_2d(position, direction)
        self.graph[position].add(target)
        if debug_mode_graph:
            print("graph grow: {} -> {}".format(position, target))
        # inversion

        if target in self.graph:
            self.graph[target].add(position)
        else:
            self.graph[target] = {position}

        return target

    def set_finish(self, target):
        self.finish = target

    def set_wall(self, target):
        self.walls.add(target)

    def find_nearest(self, position, condition):
        bfs = BFS(self.graph, position)
        return bfs.search(condition)


class BFS:

    def __init__(self, maze, position):
        self.maze = maze
        self.start = position
        self.queue = VisitQueue(position)

    def search(self, condition):
        found_with_path = {}
        while not self.queue.is_empty():
            candidate = self.queue.pop_first()
            position = candidate[0].position
            path = candidate[1] + [candidate[0].direction_idx]
            found_with_path[position] = path

            if position in self.maze.walls:
                continue

            if condition(position, self.maze.graph):
                return position, found_with_path[position]

            # expand new queue elements
            for direction_idx in dirs:
                direction = dirs[direction_idx]
                target = add_2d(position, direction)
                self.queue.add_element(target, direction_idx, path)

        return None, None

    def create_start_queue(self):
        return [(Connection(self.start, 0), [])]


class VisitQueue:
    def __init__(self, start):
        self.start = start
        self.is_starting = True
        self.queue = self.create_start_queue()
        self.already_queued = set()

    def create_start_queue(self):
        return [(Connection(self.start, 0), [])]

    def pop_first(self):
        if debug_mode_queue:
            print("Queue: popping first element {} of queue {}".format(self.queue[0], self.queue))
        return self.queue.pop(0)

    def add_element(self, target, direction_idx, current_path):
        if target not in self.already_queued:
            element = (Connection(target, direction_idx), current_path)
            self.queue.append(element)
            self.already_queued.add(target)
            if debug_mode_queue:
                print("Queue: adding element {}".format(element))
        else:
            if debug_mode_queue:
                print("Queue: not adding already visited position {}".format(target))

    def is_empty(self):
        return len(self.queue) == 0


class Connection:
    def __init__(self, position, direction_idx):
        self.position = position
        self.direction_idx = direction_idx

    def __repr__(self):
        return "Connection to {} with {}".format(self.position, self.direction_idx)


def add_2d(a, b):
    return a[0] + b[0], a[1] + b[1]


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
