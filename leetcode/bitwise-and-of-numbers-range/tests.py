import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(4, Solution().rangeBitwiseAnd(5, 7))

    def test_case2(self):
        self.assertEqual(0, Solution().rangeBitwiseAnd(0, 0))

    def test_case3(self):
        self.assertEqual(0, Solution().rangeBitwiseAnd(1, 2147483647))

    def test_case4(self):
        self.assertEqual(3, Solution().rangeBitwiseAnd(3, 3))

    def test_case5(self):
        self.assertEqual(6, Solution().rangeBitwiseAnd(6, 7))

    def test_case6(self):
        self.assertEqual(12, Solution().rangeBitwiseAnd(12, 14))
