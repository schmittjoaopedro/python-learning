import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().searchInsert([1, 3, 5, 6], 5)
        self.assertEqual(output, 2)

    def test_case2(self):
        output = Solution().searchInsert([1, 3, 5, 6], 2)
        self.assertEqual(output, 1)

    def test_case3(self):
        output = Solution().searchInsert([1, 3, 5, 6], 7)
        self.assertEqual(output, 4)

    def test_case4(self):
        output = Solution().searchInsert([1, 3, 5, 6], 0)
        self.assertEqual(output, 0)

    def test_case5(self):
        output = Solution().searchInsert([1, 3], 0)
        self.assertEqual(output, 0)

    def test_case6(self):
        output = Solution().searchInsert([3, 5, 7, 9, 10], 8)
        self.assertEqual(output, 3)
