import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(5, Solution().candy([1, 0, 2]))

    def test_case2(self):
        self.assertEqual(4, Solution().candy([1, 2, 2]))

    def test_case3(self):
        self.assertEqual(11, Solution().candy([1, 3, 4, 5, 2]))
