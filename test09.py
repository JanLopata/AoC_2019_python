import unittest

import day09 as day

test_data_part1 = """
109,2000,109,19,1102,1,102030,1985,204,-34,99;102030
109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99;109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99
1102,34915192,34915192,7,4,7,99,0;1219070632396864
104,1125899906842624,99;1125899906842624
"""


class AoCTest(unittest.TestCase):
    def test_part1(self):
        for line in test_data_part1.splitlines():
            if line == "":
                continue
            result = day.part1(line.split(";")[0])
            interpreted_result = ",".join(str(it) for it in result)
            self.assertEqual(line.split(";")[1], interpreted_result)


if __name__ == '__main__':
    unittest.main()
