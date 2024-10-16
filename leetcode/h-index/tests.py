import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, Solution().hIndex([3, 0, 6, 1, 5]))

    def test_case2(self):
        self.assertEqual(1, Solution().hIndex([1, 3, 1]))

    def test_case3(self):
        self.assertEqual(1, Solution().hIndex([100]))

    def test_case4(self):
        self.assertEqual(2, Solution().hIndex([4, 4, 0, 0]))
