import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(3,
                        left=TreeNode(1),
                        right=TreeNode(4,
                                       left=None,
                                       right=TreeNode(2)))
        self.assertEqual(1, Solution().kthSmallest(tree, 1))

    def test_case2(self):
        tree = TreeNode(5,
                        left=TreeNode(3,
                                      left=TreeNode(2,
                                                    left=TreeNode(1)),
                                      right=TreeNode(4)),
                        right=TreeNode(6))
        self.assertEqual(3, Solution().kthSmallest(tree, 3))

    def test_case3(self):
        tree = TreeNode(4,
                        left=TreeNode(2,
                                      left=None,
                                      right=TreeNode(3)),
                        right=TreeNode(5))
        self.assertEqual(2, Solution().kthSmallest(tree, 1))
