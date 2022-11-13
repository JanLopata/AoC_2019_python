import unittest

import day12 as day

test_data_1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

test_data_2 = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        result = day.compute_energy_after_n_steps(test_data_1, 10)
        self.assertEqual(179, result)

        result = day.compute_energy_after_n_steps(test_data_2, 100)
        self.assertEqual(1940, result)

    def test_part2(self):
        result = day.part2(test_data_1)
        self.assertEqual(2772, result)
        result = day.part2(test_data_2)
        self.assertEqual(4686774924, result)


if __name__ == '__main__':
    unittest.main()
