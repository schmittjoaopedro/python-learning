import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        cost = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
        self.assertEqual(cost, 5)

    def test_case2(self):
        cost = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        self.assertEqual(cost, 4)

    def test_case3(self):
        # Negative numbers
        cost = Solution().findKthLargest([-1, -3, -2, -5, -6, -4], 5)
        self.assertEqual(cost, -5)
