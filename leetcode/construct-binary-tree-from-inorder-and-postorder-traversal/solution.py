from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        preorder = postorder[::-1]
        m = {n: i for i, n in enumerate(inorder)}
        root = TreeNode(preorder[0])

        for node in preorder[1:]:
            curr = root
            while curr.val != node:
                if m[node] < m[curr.val]:  # Go left
                    if not curr.left:
                        curr.left = TreeNode(node)
                    curr = curr.left
                else:  # Go right
                    if not curr.right:
                        curr.right = TreeNode(node)
                    curr = curr.right

        return root
