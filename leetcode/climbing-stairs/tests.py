import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        cost = Solution().climbStairs(2)
        self.assertEqual(cost, 2)

    def test_case2(self):
        cost = Solution().climbStairs(3)
        self.assertEqual(cost, 3)
