import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ], Solution().generateMatrix(3))

    def test_case2(self):
        self.assertEqual([
            [1]
        ], Solution().generateMatrix(1))
