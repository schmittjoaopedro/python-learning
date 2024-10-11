import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(4,
                        left=TreeNode(2,
                                      left=TreeNode(1),
                                      right=TreeNode(3)),
                        right=TreeNode(6))

        output = Solution().getMinimumDifference(root)
        self.assertEqual(output, 1)

    def test_case2(self):
        root = TreeNode(1,
                        left=TreeNode(0),
                        right=TreeNode(48,
                                       left=TreeNode(12),
                                       right=TreeNode(49)))

        output = Solution().getMinimumDifference(root)
        self.assertEqual(output, 1)

    def test_case3(self):
        root = TreeNode(543,
                        left=TreeNode(384,
                                      right=TreeNode(445)),
                        right=TreeNode(652,
                                       right=TreeNode(699)))

        output = Solution().getMinimumDifference(root)
        self.assertEqual(output, 47)
