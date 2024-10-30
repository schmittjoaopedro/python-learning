import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, Solution().singleNumber([2, 2, 3, 2]))

    def test_case2(self):
        self.assertEqual(99, Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))
