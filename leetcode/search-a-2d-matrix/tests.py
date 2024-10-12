import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
        self.assertEqual(output, True)

    def test_case2(self):
        output = Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
        self.assertEqual(output, False)

    def test_case3(self):
        output = Solution().searchMatrix([[1]], 1)
        self.assertEqual(output, True)
