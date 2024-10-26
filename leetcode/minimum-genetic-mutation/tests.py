import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        self.assertEqual(expected, Solution().minMutation(startGene, endGene, bank))

    def test_case2(self):
        startGene = "AACCGGTT"
        endGene = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        self.assertEqual(expected, Solution().minMutation(startGene, endGene, bank))

    def test_case3(self):
        startGene = "AACCGGTT"
        endGene = "AACCGGTA"
        bank = []
        expected = -1
        self.assertEqual(expected, Solution().minMutation(startGene, endGene, bank))

    def test_case4(self):
        startGene = "AAAAAAAA"
        endGene = "CCCCCCCC"
        bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC",
                "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]
        expected = -1
        self.assertEqual(expected, Solution().minMutation(startGene, endGene, bank))

    def test_case5(self):
        startGene = "AAAAAAAT"
        endGene = "CCCCCCCC"
        bank = ["AAAAAAAC", "AAAAAAAA", "CCCCCCCC"]
        expected = -1
        self.assertEqual(expected, Solution().minMutation(startGene, endGene, bank))
