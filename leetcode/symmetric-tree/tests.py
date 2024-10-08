import unittest

from solution import Solution, Solution2, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        root = TreeNode(1,
                        left=TreeNode(2,
                                      left=TreeNode(3),
                                      right=TreeNode(4)),
                        right=TreeNode(2,
                                       left=TreeNode(4),
                                       right=TreeNode(3)))

        self.assertEqual(Solution().isSymmetric(root), True)
        self.assertEqual(Solution2().isSymmetric(root), True)

    def test_case2(self):
        root = TreeNode(1,
                        left=TreeNode(2,
                                      left=None,
                                      right=TreeNode(3)),
                        right=TreeNode(2,
                                       left=None,
                                       right=TreeNode(3)))

        self.assertEqual(Solution().isSymmetric(root), False)
        self.assertEqual(Solution2().isSymmetric(root), False)

    def test_case3(self):
        root = TreeNode(1,
                        left=TreeNode(2,
                                      left=TreeNode(2),
                                      right=None),
                        right=TreeNode(2,
                                       right=TreeNode(3)))

        self.assertEqual(Solution().isSymmetric(root), False)
        self.assertEqual(Solution2().isSymmetric(root), False)

    def test_case4(self):
        self.assertEqual(Solution().isSymmetric(TreeNode(1)), True)
        self.assertEqual(Solution2().isSymmetric(TreeNode(1)), True)
