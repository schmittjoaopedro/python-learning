import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_case2(self):
        self.assertTrue(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_case3(self):
        self.assertFalse(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
