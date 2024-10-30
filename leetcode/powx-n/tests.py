import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(1024.0, Solution().myPow(2.0, 10))

    def test_case2(self):
        self.assertEqual(0.25, Solution().myPow(2.0, -2))

    def test_case3(self):
        self.assertEqual(1.0, Solution().myPow(2.0, 0))
