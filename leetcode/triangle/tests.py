import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        cost, path = Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
        self.assertEqual(cost, 11)
        self.assertEqual(path, "2 -> 3 -> 5 -> 1")

        cost = Solution().minimumTotalDisjkstra([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
        self.assertEqual(cost, 11)

    def test_case2(self):
        cost, path = Solution().minimumTotal([[-10]])
        self.assertEqual(cost, -10)
        self.assertEqual(path, "-10")

        cost = Solution().minimumTotalDisjkstra([[-10]])
        self.assertEqual(cost, -10)

    def test_case3(self):
        cost, path = Solution().minimumTotal([[-1], [2, 3], [1, -1, -1]])
        self.assertEqual(cost, 0)
        self.assertEqual(path, "-1 -> 2 -> -1")

        cost = Solution().minimumTotalDisjkstra([[-1], [2, 3], [1, -1, -1]])
        self.assertEqual(cost, 0)

    def test_case4(self):
        cost, path = Solution().minimumTotal(
            [[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5], [3, 7, 8, -3, 7, -9],
             [-9, -1, -9, 6, 9, 0, 7], [-7, 0, -6, -8, 7, 1, -4, 9], [-3, 2, -6, -9, -7, -6, -9, 4, 0],
             [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7], [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
             [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6], [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]])
        self.assertEqual(cost, -63)
        self.assertEqual(path, "-7 -> -2 -> -5 -> -5 -> -6 -> 7 -> -9 -> -8 -> -9 -> -9 -> -2 -> -2 -> -6")

        cost = Solution().minimumTotalDisjkstra(
            [[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5], [3, 7, 8, -3, 7, -9],
             [-9, -1, -9, 6, 9, 0, 7], [-7, 0, -6, -8, 7, 1, -4, 9], [-3, 2, -6, -9, -7, -6, -9, 4, 0],
             [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7], [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
             [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6], [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]])
        self.assertEqual(cost, -63)
