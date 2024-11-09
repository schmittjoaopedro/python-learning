from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = [root.val]

        def solve(node):
            if node is None:
                return 0

            leftPath = solve(node.left)
            rightPath = solve(node.right)
            maxPath[0] = max([
                maxPath[0],
                node.val,
                node.val + leftPath,
                node.val + rightPath,
                node.val + leftPath + rightPath,
            ])

            return max(0, node.val + max(leftPath, rightPath))

        solve(root)
        return maxPath[0]
