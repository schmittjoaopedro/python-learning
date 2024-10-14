import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("fl", Solution().longestCommonPrefix(["flower", "flow", "flight"]))

    def test_case2(self):
        self.assertEqual("", Solution().longestCommonPrefix(["dog", "racecar", "car"]))
