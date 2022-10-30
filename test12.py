import unittest

import day12 as day

test_data1_part1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        result = day.compute_energy_after_n_steps(test_data1_part1, 10)
        self.assertEqual(179, result)


if __name__ == '__main__':
    unittest.main()
