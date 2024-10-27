import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        expected = [[1, 2], [1, 4], [1, 6]]
        actual = Solution().kSmallestPairs(
            [1, 7, 11],
            [2, 4, 6],
            3)
        self.assertEqual({(e[0], e[1]) for e in expected},
                         {(e[0], e[1]) for e in actual})

    def test_case2(self):
        expected = [[1, 1], [1, 1]]
        actual = Solution().kSmallestPairs(
            [1, 1, 2],
            [1, 2, 3],
            2)
        self.assertEqual({(e[0], e[1]) for e in expected},
                         {(e[0], e[1]) for e in actual})

    def test_case3(self):
        expected = [[1, 3], [2, 3], [1, 5], [2, 5], [4, 3], [1, 7], [5, 3],
                    [2, 7], [4, 5], [6, 3], [1, 9], [5, 5], [2, 9], [4, 7],
                    [6, 5], [5, 7], [4, 9], [6, 7], [5, 9], [6, 9]]
        actual = Solution().kSmallestPairs(
            [1, 2, 4, 5, 6],
            [3, 5, 7, 9],
            20)
        self.assertEqual({(e[0], e[1]) for e in expected},
                         {(e[0], e[1]) for e in actual})
