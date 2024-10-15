import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(5,
                        left=TreeNode(4,
                                      left=TreeNode(11,
                                                    left=TreeNode(7),
                                                    right=TreeNode(2))),
                        right=TreeNode(8,
                                       left=TreeNode(13),
                                       right=TreeNode(4,
                                                      right=TreeNode(1))))

        output = Solution().hasPathSum(tree, 22)
        self.assertTrue(output)

    def test_case2(self):
        tree = TreeNode(1,
                        left=TreeNode(2),
                        right=TreeNode(3))

        output = Solution().hasPathSum(tree, 5)
        self.assertFalse(output)

    def test_case3(self):
        output = Solution().hasPathSum(None, 0)
        self.assertFalse(output)
