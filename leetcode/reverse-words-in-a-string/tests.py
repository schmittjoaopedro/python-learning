import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("blue is sky the", Solution().reverseWords("the sky is blue"))

    def test_case2(self):
        self.assertEqual("world hello", Solution().reverseWords("  hello world  "))

    def test_case3(self):
        self.assertEqual("example good a", Solution().reverseWords("a good   example"))
