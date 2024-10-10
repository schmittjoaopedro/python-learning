import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        profit = Solution().maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(profit, 5)

    def test_case2(self):
        profit = Solution().maxProfit([7, 6, 4, 3, 1])
        self.assertEqual(profit, 0)

    def test_case3(self):
        profit = Solution().maxProfit([1, 2, 11, 4, 7])
        self.assertEqual(profit, 10)
