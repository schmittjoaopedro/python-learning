from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        maps = {}  # { p1: 384, p2: 445 } 61
        self.searchMinDistanceNumbers(root, maps)
        return maps["dist"]

    def searchMinDistanceNumbers(self, root, maps):
        if root:
            self.searchMinDistanceNumbers(root.left, maps)

            if "prev" not in maps:
                maps["prev"] = root.val
            else:
                if "dist" not in maps:
                    maps["dist"] = root.val - maps["prev"]
                else:
                    maps["dist"] = min(maps["dist"], root.val - maps["prev"])
                maps["prev"] = root.val

            self.searchMinDistanceNumbers(root.right, maps)
