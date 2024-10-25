import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([2, 1], Solution().absolutePermutation(2, 1))
        self.assertEqual([1, 2, 3], Solution().absolutePermutation(3, 0))
        self.assertEqual([-1], Solution().absolutePermutation(3, 2))

    def test_case2(self):
        self.assertEqual([2, 1], Solution().absolutePermutation(2, 1))
        self.assertEqual([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], Solution().absolutePermutation(10, 5))
        self.assertEqual([-1], Solution().absolutePermutation(7, 5))
        self.assertEqual([2, 1], Solution().absolutePermutation(2, 1))
        self.assertEqual([1, 2], Solution().absolutePermutation(2, 0))
        self.assertEqual([1, 2], Solution().absolutePermutation(2, 0))
        self.assertEqual([1], Solution().absolutePermutation(1, 0))
        self.assertEqual([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], Solution().absolutePermutation(10, 5))
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Solution().absolutePermutation(10, 0))
        self.assertEqual([1, 2, 3, 4, 5, 6], Solution().absolutePermutation(6, 0))
