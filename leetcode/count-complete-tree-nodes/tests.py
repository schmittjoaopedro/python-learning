import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(1,
                        left=TreeNode(2,
                                      left=TreeNode(4),
                                      right=TreeNode(5)),
                        right=TreeNode(3,
                                       left=TreeNode(6)))

        output = Solution().countNodes(tree)
        self.assertEqual(6, output)

    def test_case2(self):
        output = Solution().countNodes(None)
        self.assertEqual(0, output)

    def test_case3(self):
        output = Solution().countNodes(TreeNode(1))
        self.assertEqual(1, output)
