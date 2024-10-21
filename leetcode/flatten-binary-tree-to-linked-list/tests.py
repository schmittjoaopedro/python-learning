import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(1,
                        left=TreeNode(2,
                                      left=TreeNode(3),
                                      right=TreeNode(4)),
                        right=TreeNode(5,
                                       left=TreeNode(6)))
        output = Solution().flatten(tree)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.right.val, 2)
        self.assertEqual(output.left, None)
        self.assertEqual(output.right.right.val, 3)
        self.assertEqual(output.right.left, None)
        self.assertEqual(output.right.right.right.val, 4)
        self.assertEqual(output.right.right.left, None)
        self.assertEqual(output.right.right.right.right.val, 5)
        self.assertEqual(output.right.right.right.left, None)

    def test_case2(self):
        output = Solution().flatten(None)
        self.assertEqual(output, None)

    def test_case3(self):
        output = Solution().flatten(TreeNode(0))
        self.assertEqual(output.val, 0)
        self.assertEqual(output.right, None)
        self.assertEqual(output.left, None)
