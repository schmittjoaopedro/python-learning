import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(Solution().isHappy(19))

    def test_case2(self):
        self.assertFalse(Solution().isHappy(2))
