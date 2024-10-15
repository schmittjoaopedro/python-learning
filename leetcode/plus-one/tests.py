import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([1, 2, 4], Solution().plusOne([1, 2, 3]))

    def test_case2(self):
        self.assertEqual([4, 3, 2, 2], Solution().plusOne([4, 3, 2, 1]))

    def test_case3(self):
        self.assertEqual([1, 0], Solution().plusOne([9]))
