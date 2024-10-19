import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(6, Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_case2(self):
        self.assertEqual(9, Solution().trap([4, 2, 0, 3, 2, 5]))
