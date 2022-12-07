import os

from aoc_tools import get_data


def create_dir(name, cursor):
    cursor.add_dir(name)


def create_file(line, cursor):
    size, name = line.split(" ")
    cursor.add_file(name, int(size))


def count_tree_size(node):
    dir_size = 0
    for child in node.children.values():
        dir_size += count_tree_size(child)
    node.size_children = dir_size

    return node.size_children + node.size_files


def print_tree(node, depth=0):
    print(" " * depth, node.name, node.size_files, node.size_children)
    for file in node.files:
        print(" " * (depth + 1), file, node.files[file])
    for child in node.children.values():
        print_tree(child, depth + 1)


def transform_to_list(node, stack, result):
    deeper_node_stack = stack + [node.name]
    result.append(("/".join(deeper_node_stack), node.size()))
    for child in node.children.values():
        transform_to_list(child, deeper_node_stack, result)


def parse_tree(data):
    root = Node(None, "/")
    cursor = root
    for line in data.split("\n"):
        if line == "":
            continue

        if line.startswith("$ cd"):
            if line == "$ cd /":
                cursor = root
            elif line == "$ cd ..":
                cursor = cursor.parent
            else:
                next_dir = line.split(" ")[2]
                cursor = cursor.children[next_dir]
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            create_dir(line.split(" ")[1], cursor)
        else:
            create_file(line, cursor)
    return root


def part1(data: str):
    root = parse_tree(data)
    count_tree_size(root)

    result = []
    transform_to_list(root, [], result)

    return sum([x[1] for x in result if x[1] < 100000])


def part2(data: str):
    root = parse_tree(data)
    count_tree_size(root)

    result = []
    transform_to_list(root, [], result)

    total = 70000000
    need = 30000000
    have = total - root.size()
    to_free = need - have

    return min([x[1] for x in result if x[1] >= to_free])


class Node:
    def __init__(self, parent, name):
        self.children = {}
        self.files = {}
        self.parent = parent
        self.name = name
        self.size_files = 0
        self.size_children = None

    def add_file(self, file, size):
        self.files[file] = size
        self.size_files += size

    def add_dir(self, name):
        self.children[name] = Node(self, name)

    def size(self):
        return self.size_files + self.size_children


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
