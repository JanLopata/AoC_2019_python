import unittest

from parameterized import parameterized

import day05 as day


class AoCTest(unittest.TestCase):

    @parameterized.expand([["1002,4,3,4,33", "1002,4,3,4,99"]])
    def test_int_computer(self, program, expected):
        program_input = [int(x) for x in program.split(",")]
        program_result = ','.join([str(x) for x in day.run_program(program_input, 0, [])])
        self.assertEqual(expected, program_result)

    @parameterized.expand([[1, 0], [2, 1], [3, 0]])
    def test_1002_parameter_modes(self, position, mode):
        self.assertEqual(mode, day.mode_for_nth_parameter(1002, position))

    @parameterized.expand([[-5, 999], [0, 999], [7, 999], [8, 1000], [9, 1001], [10, 1001], [231, 1001]])
    def test_eight_comparator_program(self, input_value, output):
        program_plain = """
3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
        """
        program_input = [int(x) for x in program_plain.replace("\n", "").split(",")]
        output_values = []
        day.run_program(program_input, input_value, output_values)
        self.assertEqual(output, output_values[-1])


if __name__ == '__main__':
    unittest.main()
