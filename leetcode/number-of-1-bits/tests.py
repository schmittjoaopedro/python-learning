import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, Solution().hammingWeight(11))

    def test_case2(self):
        self.assertEqual(1, Solution().hammingWeight(128))

    def test_case3(self):
        self.assertEqual(30, Solution().hammingWeight(2147483645))
