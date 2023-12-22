import os
import queue

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def parse_component(line):
    sp = line.split(" -> ")
    targets = sp[1].split(", ")
    if sp[0] == "broadcaster":
        component = Component("c" + sp[0])
    else:
        component = Component(sp[0])

    component.add_outputs(targets)

    return component


def print_pulse(pulse):
    print("{} -{}-> {}".format(pulse[2], "high" if pulse[1] == 1 else "low", pulse[0]))


def test_button_push(data, push_times: int):
    components = init_components_from_input(data)
    ec = EventCounter()
    for i in range(push_times):
        print("=========")
        process_button_push(components, event_counter=ec)


def part1(data):
    components = init_components_from_input(data)
    ec = EventCounter()

    for i in range(1000):
        process_button_push(components, ec)

    return ec.score()


def part2(data):
    components = init_components_from_input(data)

    i = 0
    while True:
        i += 1
        if i % 10000 == 0:
            print(i)
        ec = EventCounter()
        process_button_push(components, ec)
        if ec.rx_low > 0:
            return i


class EventCounter:

    def __init__(self):
        self.high = 0
        self.low = 0
        self.rx_high = 0
        self.rx_low = 0

    def add(self, value, name):
        if value == 0:
            self.low += 1
        else:
            self.high += 1

        if name == "rx":
            if value == 0:
                self.rx_low += 1
            else:
                self.rx_high += 1

    def score(self):
        return self.low * self.high


def process_button_push(components, event_counter: EventCounter):
    pulse_queue = queue.Queue()
    pulse_queue.put(("broadcaster", 0, "button"))
    while not pulse_queue.empty():
        pulse = pulse_queue.get()
        if debug_part1:
            print_pulse(pulse)
        event_counter.add(pulse[0], pulse[1])

        if pulse[0] not in components:
            continue

        comp = components[pulse[0]]
        comp.set_input(pulse[1], pulse[2])
        if comp.process_pulse():
            for output in comp.outputs:
                pulse_queue.put((output, comp.output, comp.name))


def init_components_from_input(data):
    components = {}
    for line in data.splitlines():
        component = parse_component(line)
        components[component.name] = component
        print(component)

    missing = []
    for component in components.values():
        for output in component.outputs:
            if output not in components:
                missing.append(output)
    for missing_one in missing:
        components[missing_one] = Component('c' + missing_one)

    for component in components.values():
        for output in component.outputs:
            out_comp = components[output]
            out_comp.init_input(component.name)
    components["broadcaster"].init_input("button")
    return components


class Component:

    def __init__(self, desc: str):
        self.type = desc[0]
        self.name = desc[1:]
        self.inputs = []
        self.input_map = {}
        self.output = 0
        self.outputs = []

    def __repr__(self):
        return str((self.name, self.type, self.inputs, self.output, self.input_map, self.outputs))

    def add_outputs(self, targets):
        for x in targets:
            self.outputs.append(x)

    def init_input(self, input_name):
        idx = len(self.inputs)
        if self.type != '&' and idx > 0:
            return
        self.input_map[input_name] = idx
        self.inputs.append(0)

    def process_pulse(self):

        if self.type == 'c':
            self.output = self.inputs[0]
            return True

        if self.type == '%':
            pulse_value = self.inputs[0]
            if pulse_value == 1:
                return False
            self.output = 1 - self.output
            return True

        if self.type == '&':
            for pulse_value in self.inputs:
                if pulse_value == 0:
                    self.output = 1
                    return True

            self.output = 0
            return True

    def set_input(self, value, source):
        if self.type != '&':
            self.inputs[0] = value
        input_idx = self.input_map[source] if source in self.input_map else 0
        self.inputs[input_idx] = value


def do_tests():
    testdata1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""
    testdata2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

    # print(test_button_push(testdata1, 1))
    print(test_button_push(testdata2, 4))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
