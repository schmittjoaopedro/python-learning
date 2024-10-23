import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(2,
                        left=TreeNode(1),
                        right=TreeNode(3))
        self.assertTrue(Solution().isValidBST(tree))

    def test_case2(self):
        tree = TreeNode(5,
                        left=TreeNode(1),
                        right=TreeNode(4,
                                       left=TreeNode(3),
                                       right=TreeNode(6)))
        self.assertFalse(Solution().isValidBST(tree))
