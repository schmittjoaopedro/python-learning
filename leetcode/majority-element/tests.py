import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        resp = Solution().majorityElement1([3, 2, 3])
        self.assertEqual(resp, 3)

    def test_case2(self):
        resp = Solution().majorityElement1([2, 2, 1, 1, 1, 2, 2])
        self.assertEqual(resp, 2)

    def test_case3(self):
        resp = Solution().majorityElement1([1])
        self.assertEqual(resp, 1)

    def test_case4(self):
        resp = Solution().majorityElement1([3, 1, 2, 1, 4, 1])
        self.assertEqual(resp, 1)
