import unittest

from solution import WordDictionary


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        wdict = WordDictionary()
        wdict.addWord("bad")
        wdict.addWord("dad")
        wdict.addWord("mad")
        self.assertFalse(wdict.search("pad"))
        self.assertTrue(wdict.search("bad"))
        self.assertTrue(wdict.search(".ad"))
        self.assertTrue(wdict.search("b.."))

    def test_case2(self):
        wd = WordDictionary()
        wd.addWord("at")
        wd.addWord("and")
        wd.addWord("an")
        wd.addWord("add")
        self.assertFalse(wd.search("a"))
        self.assertFalse(wd.search(".at"))
        wd.addWord("bat")
        self.assertTrue(wd.search(".at"))
        self.assertTrue(wd.search("an."))
        self.assertFalse(wd.search("a.d."))
        self.assertFalse(wd.search("b."))
        self.assertTrue(wd.search("a.d"))
        self.assertFalse(wd.search("."))
