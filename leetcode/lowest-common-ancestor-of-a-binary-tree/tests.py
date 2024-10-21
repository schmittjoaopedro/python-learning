import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(3,
                        left=TreeNode(5,
                                      left=TreeNode(6),
                                      right=TreeNode(2,
                                                     left=TreeNode(7),
                                                     right=TreeNode(4))),
                        right=TreeNode(1,
                                       left=TreeNode(0),
                                       right=TreeNode(8)))
        self.assertEqual(3, Solution().lowestCommonAncestor(tree, TreeNode(5), TreeNode(1)).val)

    def test_case2(self):
        tree = TreeNode(3,
                        left=TreeNode(5,
                                      left=TreeNode(6),
                                      right=TreeNode(2,
                                                     left=TreeNode(7),
                                                     right=TreeNode(4))),
                        right=TreeNode(1,
                                       left=TreeNode(0),
                                       right=TreeNode(8)))
        self.assertEqual(5, Solution().lowestCommonAncestor(tree, TreeNode(5), TreeNode(4)).val)

    def test_case3(self):
        tree = TreeNode(1,
                        left=TreeNode(2))
        self.assertEqual(1, Solution().lowestCommonAncestor(tree, TreeNode(1), TreeNode(2)).val)
