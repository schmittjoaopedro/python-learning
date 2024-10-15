from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def solve(node, prev):
            curr = node.val + prev
            if not node.left and not node.right:
                return curr == targetSum

            if node.left and solve(node.left, curr):
                return True
            if node.right and solve(node.right, curr):
                return True
            return False

        return solve(root, 0)
