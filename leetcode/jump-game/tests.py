import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().canJump([2, 3, 1, 1, 4])
        self.assertEqual(output, True)

    def test_case2(self):
        output = Solution().canJump([3, 2, 1, 0, 4])
        self.assertEqual(output, False)
