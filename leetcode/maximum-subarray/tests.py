import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(output, 6)

    def test_case2(self):
        output = Solution().maxSubArray([1])
        self.assertEqual(output, 1)

    def test_case3(self):
        output = Solution().maxSubArray([5, 4, -1, 7, 8])
        self.assertEqual(output, 23)
