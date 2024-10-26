import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
                         Solution().letterCombinations("23"))

    def test_case2(self):
        self.assertEqual([], Solution().letterCombinations(""))

    def test_case3(self):
        self.assertEqual(["a", "b", "c"], Solution().letterCombinations("2"))
