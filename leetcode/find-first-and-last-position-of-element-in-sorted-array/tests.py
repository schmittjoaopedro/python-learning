import io
import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([3, 4], Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

    def test_case2(self):
        self.assertEqual([-1, -1], Solution().searchRange([5, 7, 7, 8, 8, 10], 6))

    def test_case3(self):
        self.assertEqual([-1, -1], Solution().searchRange([], 0))
