import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(1, Solution().findMin([3, 4, 5, 1, 2]))

    def test_case2(self):
        self.assertEqual(0, Solution().findMin([4, 5, 6, 7, 0, 1, 2]))

    def test_case3(self):
        self.assertEqual(11, Solution().findMin([11, 13, 15, 17]))

    def test_case4(self):
        self.assertEqual(1, Solution().findMin([3, 1, 2]))

    def test_case5(self):
        self.assertEqual(1, Solution().findMin([5, 1, 2, 3, 4]))
