def part1(data: str):
    pair = data.split("-")
    low = int(pair[0])
    high = int(pair[1])

    counter = 0
    for n in range(low, high + 1):
        if check_criterias(n):
            counter += 1

    return counter


def part2(data: str):
    pair = data.split("-")
    low = int(pair[0])
    high = int(pair[1])

    counter = 0
    for n in range(low, high + 1):
        if additional_crit(n):
            counter += 1

    return counter


def is_double(tup):
    return tup[1] - tup[0] == 2


def check_criterias(n):
    digits = [int(n / 10 ** (5 - x)) % 10 for x in range(6)]
    has_double = False
    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False

        if not has_double:
            has_double = digits[i + 1] == digits[i]

    return has_double


def additional_crit(n):
    digits = [int(n / 10 ** (5 - x)) % 10 for x in range(6)]

    repeats = []
    active = 0

    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            return False

        if digits[i + 1] != digits[active]:
            repeats.append((active, i + 1))
            active = i + 1

    repeats.append((active, len(digits)))
    doubles = [x for x in filter(is_double, repeats)]
    return len(doubles) > 0


if __name__ == "__main__":
    # this_filename = os.path.basename(__file__)
    # input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = "156218-652527"
    # print(input_filename)

    print(part1(data))
    print(part2(data))
