import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(3,
                        left=TreeNode(9),
                        right=TreeNode(20,
                                       left=TreeNode(15),
                                       right=TreeNode(7)))
        expected = [[3], [20, 9], [15, 7]]
        self.assertEqual(expected, Solution().zigzagLevelOrder(tree))

    def test_case2(self):
        tree = TreeNode(1)
        expected = [[1]]
        self.assertEqual(expected, Solution().zigzagLevelOrder(tree))

    def test_case3(self):
        tree = None
        expected = []
        self.assertEqual(expected, Solution().zigzagLevelOrder(tree))

    def test_case4(self):
        tree = TreeNode(-2,
                        left=TreeNode(0,
                                      left=None,
                                      right=TreeNode(3,
                                                     left=TreeNode(6),
                                                     right=None)),
                        right=TreeNode(-1,
                                       left=TreeNode(0,
                                                     left=TreeNode(5),
                                                     right=TreeNode(-5)),
                                       right=None))
        expected = [[-2], [-1, 0], [3, 0], [-5, 5, 6]]
        self.assertEqual(expected, Solution().zigzagLevelOrder(tree))
