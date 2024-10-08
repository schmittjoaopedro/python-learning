import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(val=1,
                        left=TreeNode(val=2,
                                      right=TreeNode(val=5)),
                        right=TreeNode(val=3,
                                       right=TreeNode(val=4)))
        right_most = Solution().rightSideView(tree)
        self.assertEqual(right_most, [1, 3, 4])

    def test_case2(self):
        tree = TreeNode(val=1,
                        right=TreeNode(val=3))
        right_most = Solution().rightSideView(tree)
        self.assertEqual(right_most, [1, 3])

    def test_case3(self):
        right_most = Solution().rightSideView(None)
        self.assertEqual(right_most, [])
