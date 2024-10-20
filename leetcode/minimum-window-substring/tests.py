import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("BANC", Solution().minWindow("ADOBECODEBANC", "ABC"))

    def test_case2(self):
        self.assertEqual("a", Solution().minWindow("a", "a"))

    def test_case3(self):
        self.assertEqual("", Solution().minWindow("a", "aa"))

    def test_case4(self):
        self.assertEqual("", Solution().minWindow("a", "b"))

    def test_case5(self):
        self.assertEqual("a", Solution().minWindow("ab", "a"))

    def test_case6(self):
        self.assertEqual("ab", Solution().minWindow("abc", "ab"))

    def test_case7(self):
        self.assertEqual("dbaa", Solution().minWindow("acbdbaab", "aabd"))
