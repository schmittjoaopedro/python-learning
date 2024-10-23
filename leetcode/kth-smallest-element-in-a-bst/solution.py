from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        counter = 0

        def search(node):
            nonlocal counter
            ret = None
            if node.left:
                ret = search(node.left)
            counter += 1
            if counter == k:
                ret = node.val
            if node.right and ret is None:
                ret = search(node.right)
            return ret

        return search(root)
