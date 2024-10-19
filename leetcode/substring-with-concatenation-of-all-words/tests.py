import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([0, 9], Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))

    def test_case2(self):
        self.assertEqual([], Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))

    def test_case3(self):
        self.assertEqual([6, 9, 12], Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

    def test_case4(self):
        self.assertEqual([8], Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
