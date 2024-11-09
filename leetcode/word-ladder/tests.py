import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(5, Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

    def test_case2(self):
        self.assertEqual(0, Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

    def test_case3(self):
        self.assertEqual(0, Solution().ladderLength("hot", "cog", ["hot", "dog"]))
