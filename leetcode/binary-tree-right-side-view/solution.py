from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_most = []
        self.deepSearch(root, right_most, 1)
        return right_most

    def deepSearch(self, node, right_most, depth):
        if node:
            if len(right_most) < depth:
                right_most.append(node.val)
            else:
                right_most[depth - 1] = node.val
            self.deepSearch(node.left, right_most, depth + 1)
            self.deepSearch(node.right, right_most, depth + 1)
