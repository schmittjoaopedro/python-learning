import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        cost = Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        self.assertEqual(cost, 7)

    def test_case2(self):
        cost = Solution().minPathSum([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(cost, 12)
