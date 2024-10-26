import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
                         Solution().permute([1, 2, 3]))

    def test_case2(self):
        self.assertEqual([[0, 1], [1, 0]],
                         Solution().permute([0, 1]))

    def test_case3(self):
        self.assertEqual([[1]],
                         Solution().permute([1]))
