import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

XMAS_INDICES = {"x": 0, "m": 1, "a": 2, "s": 3}


def load_data(data):
    sp = data.split("\n\n")
    workflows = {}
    parts = []
    for line in sp[0].splitlines():
        workflow = Workflow(line)
        label = workflow.label
        workflows[label] = workflow

    for line in sp[1].splitlines():
        parts.append(WfPart(line))

    return workflows, parts


def part1(data):
    workflows, parts = load_data(data)
    if debug_part1:
        print(workflows)
        print(parts)

    result = 0
    for part in parts:

        wfl = "in"
        s = wfl
        while wfl not in ["A", "R"]:
            wf = workflows[wfl]
            wfl = wf.process_part(part)
            s += " -> " + wfl

        if wfl == "A":
            result += part.score()

        if debug_part1:
            print(part, s)

    return result


def part2(data):
    pass


class WfPart:

    def __init__(self, line: str):
        self.line = line
        s1 = line.replace("{", "").replace("}", "").split(",")
        s2 = [x.split("=")[1] for x in s1]
        self.values = [int(x) for x in s2]

    def score(self):
        return sum(self.values)

    def __repr__(self):
        return str(self.values)


class Workflow:

    def __init__(self, line: str):
        self.line = line
        sp1 = line.split("{")
        self.label = sp1[0]
        sp2 = sp1[1].replace("}", "").split(",")
        self.rules = [Rule(x) for x in sp2]

    def process_part(self, part: WfPart):
        for rule in self.rules:
            if rule.matches(part):
                return rule.match_exit


class Rule:

    def __init__(self, desc: str):
        sp = desc.split(":")
        self.conditioned = len(sp) > 1

        if self.conditioned:
            self.greater = ">" in sp[0]
            self.match_exit = sp[1]
            self.var_idx = XMAS_INDICES[sp[0][0]]
            self.cond_value = int(sp[0][2:])
        else:
            self.match_exit = sp[0]

    def __repr__(self):
        if self.conditioned:
            return str((self.match_exit, self.var_idx, self.greater, self.cond_value))
        else:
            return str(self.match_exit)

    def matches(self, part: WfPart):
        if self.conditioned:
            if self.greater:
                return part.values[self.var_idx] > self.cond_value
            else:
                return part.values[self.var_idx] < self.cond_value
        return True


def do_tests():
    testdata1 = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
