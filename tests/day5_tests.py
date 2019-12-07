import unittest
from day5 import TEST


class MyTestCase(unittest.TestCase):
    def test_part1(self):
        arr = [1002, 4, 3, 4, 33]
        test = TEST(arr)
        test.run()
        self.assertEqual(test.intcode, [1002, 4, 3, 4, 99])

    def test_part2_equal_8_true(self):
        arr = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        test = TEST(arr, 8)
        test.run()
        self.assertEqual(test.log, [1])

    def test_part2_equal_8_false(self):
        arr = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        test = TEST(arr,  5)
        test.run()
        self.assertEqual(test.log, [0])

    def test_part2_less_than_8_true(self):
        arr = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        test = TEST(arr, 7)
        test.run()
        self.assertEqual(test.log, [1])

    def test_part2_less_than_8_false(self):
        arr = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        test = TEST(arr, 9)
        test.run()
        self.assertEqual(test.log, [0])

    def test_part2_imm_equal_8_true(self):
        arr = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        test = TEST(arr, 8)
        test.run()
        self.assertEqual(test.log, [1])

    def test_part2_imm_equal_8_false(self):
        arr = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        test = TEST(arr, 3)
        test.run()
        self.assertEqual(test.log, [0])

    def test_part2_imm_less_than_8_true(self):
        arr = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        test = TEST(arr, 7)
        test.run()
        self.assertEqual(test.log, [1])

    def test_part2_imm_less_than_8_false(self):
        arr = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        test = TEST(arr, 9)
        test.run()
        self.assertEqual(test.log, [0])

    def test_part2_pos_inp_zero(self):
        arr = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        test = TEST(arr, 0)
        test.run()
        self.assertEqual(test.log, [0])

    def test_part2_pos_inp_nonzero(self):
        arr = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        test = TEST(arr, 5)
        test.run()
        self.assertEqual(test.log, [1])

    def test_part2_large_below8(self):
        arr = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
               20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        test = TEST(arr, 7)
        test.run()
        self.assertEqual(test.log, [999])

    def test_part2_large_equal8(self):
        arr = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
               20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        test = TEST(arr, 8)
        test.run()
        self.assertEqual(test.log, [1000])

    def test_part2_large_above8(self):
        arr = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125,
               20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        test = TEST(arr, 9)
        test.run()
        self.assertEqual(test.log, [1001])


if __name__ == '__main__':
    unittest.main()
