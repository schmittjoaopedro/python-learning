import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        board = [[0, 1, 0],
                 [0, 0, 1],
                 [1, 1, 1],
                 [0, 0, 0]]
        Solution().gameOfLife(board)
        self.assertEqual(
            [[0, 0, 0],
             [1, 0, 1],
             [0, 1, 1],
             [0, 1, 0]], board)

    def test_case2(self):
        board = [[1, 1],
                 [1, 0]]
        Solution().gameOfLife(board)
        self.assertEqual(
            [[1, 1],
             [1, 1]], board)
