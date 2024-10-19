import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("MMMDCCXLIX", Solution().intToRoman(3749))

    def test_case2(self):
        self.assertEqual("LVIII", Solution().intToRoman(58))

    def test_case3(self):
        self.assertEqual("MCMXCIV", Solution().intToRoman(1994))
