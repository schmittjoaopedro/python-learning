from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0

        def sumNode(node, acc):
            localSum = acc * 10 + node.val
            if not node.left and not node.right:
                nonlocal total
                total += localSum
            else:
                if node.left:
                    sumNode(node.left, localSum)
                if node.right:
                    sumNode(node.right, localSum)

        sumNode(root, 0)
        return total
