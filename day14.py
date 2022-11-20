import os

import requests


def part1(data: str):
    pass


def part2(data: str):
    pass


def download_data(day_number, input_filename):
    url = f"https://adventofcode.com/2019/day/{day_number}/input"
    cookies = {"session": os.environ["AOC_SESSION"]}
    print(cookies)
    print(url)

    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    print(response.text)
    with open(input_filename, "w") as input_file:
        input_file.write(response.text)


def get_data():
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    parsed_number = int(this_filename.replace("day", "").replace(".py", ""))

    try:
        return read_data(input_filename)
    except FileNotFoundError:
        download_data(parsed_number, input_filename)


def read_data(input_filename):
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    data = get_data()
    # print(input_filename)

    print(part1(data))
    print(part2(data))
