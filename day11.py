import math
import os

from aoc_tools import get_data


def parse_monkey(block):
    monkey = Monkey()
    for line in block.split("\n"):
        if line.startswith("Monkey"):
            monkey.id = int(line.split(" ")[1][:-1])

        if line.startswith("  Starting"):
            sp = line.split(":")
            monkey.items = [int(x) for x in sp[1].strip().split(", ")]

        if line.startswith("  Operation"):
            sp = line.split(":")
            monkey.operation_parameters = sp[1].strip().split(" ")

        if line.startswith("  Test"):
            sp = line.split(":")
            monkey.divisor = int(sp[1].strip().split(" ")[2])

        if line.startswith("    If true"):
            sp = line.split(":")
            monkey.targets[1] = int(sp[1].strip().split(" ")[3])

        if line.startswith("    If false"):
            sp = line.split(":")
            monkey.targets[0] = int(sp[1].strip().split(" ")[3])

    monkey.build_operation()
    return monkey


def part1(data: str):
    blocks = data.split("\n\n")
    monkeys = []
    for block in blocks:
        monkey = parse_monkey(block)
        monkeys.append(monkey)

    lcm = compute_monkeys_lcm(monkeys)

    for i in range(20):
        do_round(monkeys, lcm)

    inspections = [monkey.inspect_counter for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def do_round(monkeys, lcm):
    for monkey in monkeys:

        shuffles = []
        while len(monkey.items) > 0:
            shuffles.append(monkey.process_one_item())

        for move in shuffles:
            target = monkeys[move[0]]
            received_item = move[1] % lcm
            target.items.append(received_item)


def compute_monkeys_lcm(monkeys):
    # compute least common multiple of all divisors
    divisors = [monkey.divisor for monkey in monkeys]
    lcm = divisors[0]
    for i in range(1, len(divisors)):
        lcm = lcm * divisors[i] // math.gcd(lcm, divisors[i])
    return lcm


def part2(data: str):
    blocks = data.split("\n\n")
    monkeys = []
    for block in blocks:
        monkey = parse_monkey(block)
        monkeys.append(monkey)

    for monkey in monkeys:
        monkey.bored_divisor = 1

    lcm = compute_monkeys_lcm(monkeys)

    for i in range(10000):

        if i % 100 == 0:
            print("Progress: {}%".format(i / 100))
        do_round(monkeys, lcm)

    inspections = [monkey.inspect_counter for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


class Monkey:
    def __init__(self):
        self.id = None
        self.items = []
        self.operation_parameters = []
        self.operation_lambda = None
        self.divisor = None
        self.targets = [-1, -1]
        self.bored_divisor = 3
        self.inspect_counter = 0

    def __str__(self):
        return f"Monkey {self.id} with items {self.items}, OpPars: {self.operation_parameters}, OpLambda: {self.operation_lambda}, Divisor: {self.divisor}, Targets: {self.targets}"

    def build_operation(self):
        right_side = " ".join(self.operation_parameters[2:])
        self.operation_lambda = (lambda old: eval(right_side))

    def process_one_item(self):
        self.inspect_counter += 1
        worry = self.items.pop(0)

        worry = self.operation_lambda(worry)
        # worry = hardcoded_ops_test(worry, self.id)
        if self.bored_divisor != 1:
            worry = worry // self.bored_divisor

        target_monkey = self.targets[worry % self.divisor == 0]
        return target_monkey, worry


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
