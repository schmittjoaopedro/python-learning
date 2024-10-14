import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(5, Solution().lengthOfLastWord("Hello World"))

    def test_case2(self):
        self.assertEqual(4, Solution().lengthOfLastWord("   fly me   to   the moon  "))

    def test_case3(self):
        self.assertEqual(6, Solution().lengthOfLastWord("luffy is still joyboy"))
