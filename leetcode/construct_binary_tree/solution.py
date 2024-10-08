from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxs = {n: i for i, n in enumerate(inorder)}
        root = TreeNode(val=preorder[0])

        for val in preorder[1:]:
            self.addNode(root, val, idxs)
        return root

    def addNode(self, root, val, idxs):
        if idxs[val] < idxs[root.val]:
            if root.left:
                self.addNode(root.left, val, idxs)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.addNode(root.right, val, idxs)
            else:
                root.right = TreeNode(val)
