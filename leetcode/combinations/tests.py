import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                         Solution().combine(4, 2))

    def test_case2(self):
        self.assertEqual([[1]],
                         Solution().combine(1, 1))
