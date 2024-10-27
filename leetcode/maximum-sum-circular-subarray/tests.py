import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, Solution().maxSubarraySumCircular([1, -2, 3, -2]))

    def test_case2(self):
        self.assertEqual(10, Solution().maxSubarraySumCircular([5, -3, 5]))

    def test_case3(self):
        self.assertEqual(-2, Solution().maxSubarraySumCircular([-3, -2, -3]))

    def test_case4(self):
        self.assertEqual(4, Solution().maxSubarraySumCircular([3, -1, 2, -1]))
