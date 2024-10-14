import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, Solution().romanToInt("III"))

    def test_case2(self):
        self.assertEqual(58, Solution().romanToInt("LVIII"))

    def test_case3(self):
        self.assertEqual(1994, Solution().romanToInt("MCMXCIV"))
