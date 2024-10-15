import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().mySqrt(4))

    def test_case2(self):
        self.assertEqual(2, Solution().mySqrt(8))

    def test_case3(self):
        self.assertEqual(0, Solution().mySqrt(0))

    def test_case4(self):
        self.assertEqual(1, Solution().mySqrt(2))

    def test_case5(self):
        self.assertEqual(1, Solution().mySqrt(3))

