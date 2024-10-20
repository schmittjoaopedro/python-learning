import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(4, Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test_case2(self):
        self.assertEqual(0, Solution().longestConsecutive([]))

    def test_case3(self):
        self.assertEqual(9, Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
