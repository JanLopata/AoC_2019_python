import unittest

from parameterized import parameterized

import day02 as day


class AoCTest(unittest.TestCase):

    @parameterized.expand([["1,9,10,3,2,3,11,0,99,30,40,50", "3500,9,10,70,2,3,11,0,99,30,40,50"]])
    def test_fuel_req(self, program, expected):
        program_input = [int(x) for x in program.split(",")]
        program_result = ','.join([str(x) for x in day.run_program(program_input)])
        self.assertEqual(expected, program_result)


if __name__ == '__main__':
    unittest.main()
