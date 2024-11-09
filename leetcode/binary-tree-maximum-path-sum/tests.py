import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(1,
                        left=TreeNode(2),
                        right=TreeNode(3))
        self.assertEqual(6, Solution().maxPathSum(tree))

    def test_case2(self):
        tree = TreeNode(-10,
                        left=TreeNode(9),
                        right=TreeNode(20,
                                       left=TreeNode(15),
                                       right=TreeNode(7)))
        self.assertEqual(42, Solution().maxPathSum(tree))

    def test_case3(self):
        tree = TreeNode(-3)
        self.assertEqual(-3, Solution().maxPathSum(tree))

    def test_case4(self):
        tree = TreeNode(9,
                        left=TreeNode(6),
                        right=TreeNode(-3,
                                       left=TreeNode(-6),
                                       right=TreeNode(2,
                                                      left=TreeNode(2,
                                                                    left=TreeNode(-6,
                                                                                  left=TreeNode(-6)),
                                                                    right=TreeNode(-6)))))
        self.assertEqual(16, Solution().maxPathSum(tree))
