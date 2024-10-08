import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
        self.assertEqual(tree.val, 3)
        self.assertEqual(tree.left.val, 9)
        self.assertEqual(tree.right.val, 20)
        self.assertEqual(tree.right.left.val, 15)
        self.assertEqual(tree.right.right.val, 7)

    def test_case2(self):
        tree = Solution().buildTree(preorder=[-1], inorder=[-1])
        self.assertEqual(tree.val, -1)

    def test_case3(self):
        tree = Solution().buildTree(preorder=[3, 1, 2, 4], inorder=[1, 2, 3, 4])
        self.assertEqual(tree.val, 3)
        self.assertEqual(tree.left.val, 1)
        self.assertEqual(tree.left.right.val, 2)
        self.assertEqual(tree.right.val, 4)
