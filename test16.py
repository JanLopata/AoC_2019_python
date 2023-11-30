import unittest

import day14 as day

test_data_part1 = """
"""


def max_size(data: list):
    return max(abs(x) for sublist in data for x in sublist)


class AoCTest(unittest.TestCase):

    def test_part1(self):
        examples = test_data_part1.split("\n\n")
        for example in examples:
            spl = example.split("\n;\n")
            result = day.part1(spl[0])
            self.assertEqual(int(spl[1]), result)


if __name__ == '__main__':
    unittest.main()
