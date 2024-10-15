from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def solve(node):
            n1, n2 = 0, 0
            if node.left:
                n1 = solve(node.left)
            if node.right:
                n2 = solve(node.right)
            return 1 + n1 + n2

        return solve(root)
