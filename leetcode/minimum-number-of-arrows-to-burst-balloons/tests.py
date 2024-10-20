import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))

    def test_case2(self):
        self.assertEqual(4, Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))

    def test_case3(self):
        self.assertEqual(2, Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))

    def test_case4(self):
        self.assertEqual(2, Solution().findMinArrowShots(
            [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))

    def test_case5(self):
        self.assertEqual(2, Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
