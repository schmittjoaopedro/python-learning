import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().jump([2, 3, 1, 1, 4]))

    def test_case2(self):
        self.assertEqual(2, Solution().jump([2, 3, 0, 1, 4]))

    def test_case3(self):
        self.assertEqual(1, Solution().jump([2, 1]))

    def test_case4(self):
        self.assertEqual(5, Solution().jump([
            5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5,
            2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]))
