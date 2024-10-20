import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
        self.assertEqual(output.val, 3)
        self.assertEqual(output.left.val, 9)
        self.assertEqual(output.right.val, 20)
        self.assertEqual(output.right.left.val, 15)
        self.assertEqual(output.right.right.val, 7)

    def test_case2(self):
        output = Solution().buildTree([-1], [-1])
        self.assertEqual(output.val, -1)
