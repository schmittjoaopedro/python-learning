import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([24, 12, 8, 6], Solution().productExceptSelf([1, 2, 3, 4]))

    def test_case2(self):
        self.assertEqual([0, 0, 9, 0, 0], Solution().productExceptSelf([-1, 1, 0, -3, 3]))
