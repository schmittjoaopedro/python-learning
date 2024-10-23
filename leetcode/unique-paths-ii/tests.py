import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]))

    def test_case2(self):
        self.assertEqual(1, Solution().uniquePathsWithObstacles([
            [0, 1],
            [0, 0]
        ]))

    def test_case3(self):
        self.assertEqual(0, Solution().uniquePathsWithObstacles([
            [0, 0],
            [0, 1]
        ]))
