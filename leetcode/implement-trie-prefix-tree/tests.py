import unittest

from solution import Trie


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))
