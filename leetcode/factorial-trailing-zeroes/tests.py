import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(0, Solution().trailingZeroes(3))

    def test_case2(self):
        self.assertEqual(1, Solution().trailingZeroes(5))

    def test_case3(self):
        self.assertEqual(0, Solution().trailingZeroes(0))

    def test_case4(self):
        self.assertEqual(7, Solution().trailingZeroes(30))
