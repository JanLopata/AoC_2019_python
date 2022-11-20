import os

import requests

debug_input_data_download = False


def read_cookie_from_file():
    with open("input/cookie.txt") as cookie_file:
        return cookie_file.read().strip()


def download_data(day_number, input_filename):
    url = f"https://adventofcode.com/2019/day/{day_number}/input"
    cookies = {"session": read_cookie_from_file()}
    if debug_input_data_download:
        print(cookies)
        print(url)

    response = requests.get(url, cookies=cookies)
    response.raise_for_status()

    if debug_input_data_download:
        print(response.text)
    with open(input_filename, "w") as input_file:
        input_file.write(response.text)


def get_data(this_filename: str):
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    parsed_number = int(this_filename.replace("day", "").replace(".py", ""))

    try:
        return read_data(input_filename)
    except FileNotFoundError:
        download_data(parsed_number, input_filename)
        return read_data(input_filename)


def read_data(input_filename):
    with open(input_filename) as input_file:
        return input_file.read()
