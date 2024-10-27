import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(4, Solution().search([4, 5, 6, 7, 0, 1, 2], 0))

    def test_case2(self):
        self.assertEqual(-1, Solution().search([4, 5, 6, 7, 0, 1, 2], 3))

    def test_case3(self):
        self.assertEqual(-1, Solution().search([1], 0))

    def test_case4(self):
        self.assertEqual(0, Solution().search([5, 1, 3], 5))

    def test_case5(self):
        self.assertEqual(1, Solution().search([5, 1, 2, 3, 4], 1))
