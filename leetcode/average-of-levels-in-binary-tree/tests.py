import unittest

from solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = TreeNode(3,
                        left=TreeNode(9),
                        right=TreeNode(20,
                                       left=TreeNode(15),
                                       right=TreeNode(7)))

        output = Solution().averageOfLevels(tree)
        self.assertEqual([3.0, 14.5, 11.0], output)

    def test_case2(self):
        tree = TreeNode(3,
                        left=TreeNode(9,
                                      left=TreeNode(15),
                                      right=TreeNode(7)),
                        right=TreeNode(20))

        output = Solution().averageOfLevels(tree)
        self.assertEqual([3.0, 14.5, 11.0], output)
