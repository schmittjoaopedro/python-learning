import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(1,
                        left=TreeNode(2),
                        right=TreeNode(3))
        self.assertEqual(25, Solution().sumNumbers(tree))

    def test_case2(self):
        tree = TreeNode(4,
                        left=TreeNode(9,
                                      left=TreeNode(5),
                                      right=TreeNode(1)),
                        right=TreeNode(0))
        self.assertEqual(1026, Solution().sumNumbers(tree))
