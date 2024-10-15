import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(1, Solution().singleNumber([2, 2, 1]))

    def test_case2(self):
        self.assertEqual(4, Solution().singleNumber([4, 1, 2, 1, 2]))

    def test_case3(self):
        self.assertEqual(1, Solution().singleNumber([1]))
