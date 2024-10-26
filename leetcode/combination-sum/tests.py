import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([[2, 2, 3], [7]], Solution().combinationSum([2, 3, 6, 7], 7))

    def test_case2(self):
        self.assertEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], Solution().combinationSum([2, 3, 5], 8))

    def test_case3(self):
        self.assertEqual([], Solution().combinationSum([2], 1))
