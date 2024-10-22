import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(3,
                        left=TreeNode(9),
                        right=TreeNode(20,
                                       left=TreeNode(15),
                                       right=TreeNode(7)))
        expected = [[3], [9, 20], [15, 7]]
        self.assertEqual(expected, Solution().levelOrder(tree))

    def test_case2(self):
        tree = TreeNode(1)
        expected = [[1]]
        self.assertEqual(expected, Solution().levelOrder(tree))

    def test_case3(self):
        tree = None
        expected = []
        self.assertEqual(expected, Solution().levelOrder(tree))
