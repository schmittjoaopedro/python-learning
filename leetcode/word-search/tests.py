import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertTrue(Solution().exist(board, word))

    def test_case2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(Solution().exist(board, word))

    def test_case3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertFalse(Solution().exist(board, word))
