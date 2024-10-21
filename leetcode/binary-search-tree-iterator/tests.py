import unittest

from solution import BSTIterator, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(7,
                        left=TreeNode(3),
                        right=TreeNode(15,
                                       left=TreeNode(9),
                                       right=TreeNode(20)))
        iterator = BSTIterator(tree)
        self.assertEqual(3, iterator.next())
        self.assertEqual(7, iterator.next())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(9, iterator.next())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(15, iterator.next())
        self.assertTrue(iterator.hasNext())
        self.assertEqual(20, iterator.next())
        self.assertFalse(iterator.hasNext())
