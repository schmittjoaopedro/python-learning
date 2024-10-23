from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def solve(node):
            if not node:
                return None, None, True

            minL, maxL, valL = solve(node.left)
            if not valL:
                return None, None, False

            minR, maxR, valR = solve(node.right)
            if not valR:
                return None, None, False

            if minL is None and maxL is None:
                minL, maxL = node.val, node.val
                valL = True
            else:
                valL = maxL < node.val

            if minR is None and maxR is None:
                minR, maxR = node.val, node.val
                valR = True
            else:
                valR = node.val < minR

            return minL, maxR, valL and valR

        return solve(root)[2]
