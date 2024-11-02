import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(4, Solution().rob([1, 2, 3, 1]))

    def test_case2(self):
        self.assertEqual(12, Solution().rob([2, 7, 9, 3, 1]))
