from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> TreeNode | None:
        if not root:
            return None

        def preorder(node):
            if not node.left and not node.right:
                return node

            left = node.left
            right = node.right

            if left and right:
                last = preorder(left)
                node.left = None
                node.right = left
                last.right = right
                return preorder(right)
            elif left:
                last = preorder(left)
                node.left = None
                node.right = left
                return last
            else:
                return preorder(right)

        preorder(root)
        return root
