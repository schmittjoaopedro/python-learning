import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().findPeakElement([1, 2, 3, 1]))

    def test_case2(self):
        self.assertEqual(5, Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))

    def test_case3(self):
        self.assertEqual(1, Solution().findPeakElement([3, 4, 3, 2, 1]))

    def test_case4(self):
        self.assertEqual(1, Solution().findPeakElement([1, 6, 5, 4, 3, 2, 1]))
