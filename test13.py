import unittest

import day13 as day

test_data_part1 = """
1,2,3,6,5,4;2
"""


def max_size(data: list):
    return max(abs(x) for sublist in data for x in sublist)


class AoCTest(unittest.TestCase):

    def test_part1(self):
        # invalid test!
        for line in test_data_part1.splitlines():
            if line == "":
                continue
            result = day.part1(line.split(";")[0])
            self.assertEqual(line.split(";")[1], result)


if __name__ == '__main__':
    unittest.main()
