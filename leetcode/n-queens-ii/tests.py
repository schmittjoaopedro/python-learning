import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().totalNQueens(4))

    def test_case2(self):
        self.assertEqual(1, Solution().totalNQueens(1))

    def test_case3(self):
        self.assertEqual(352, Solution().totalNQueens(9))

    def test_case4(self):
        self.assertEqual(14200, Solution().totalNQueens(12))

    def test_case5(self):
        self.assertEqual(73712, Solution().totalNQueens(13))
