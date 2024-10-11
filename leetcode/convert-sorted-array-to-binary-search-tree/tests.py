import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
        self.assertEqual(output.val, 0)
        self.assertEqual(output.left.val, -3)
        self.assertEqual(output.left.left.val, -10)
        self.assertEqual(output.right.val, 5)
        self.assertEqual(output.right.right.val, 9)

    def test_case2(self):
        output = Solution().sortedArrayToBST([1, 3])
        self.assertEqual(output.val, 3)
        self.assertEqual(output.left.val, 1)
