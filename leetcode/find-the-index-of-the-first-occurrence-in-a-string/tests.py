import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(0, Solution().strStr("sadbutsad", "sad"))

    def test_case2(self):
        self.assertEqual(-1, Solution().strStr("leetcode", "leeto"))

    def test_case3(self):
        self.assertEqual(2, Solution().strStr("hello", "ll"))

    def test_case4(self):
        self.assertEqual(0, Solution().strStr("a", "a"))
