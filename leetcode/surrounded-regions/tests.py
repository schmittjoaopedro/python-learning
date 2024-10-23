import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        Solution().solve(board)
        self.assertEqual([
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ], board)

    def test_case2(self):
        board = [["X"]]
        Solution().solve(board)
        self.assertEqual([["X"]], board)
