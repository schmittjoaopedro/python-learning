from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]

        nodes = [root]
        avgs = [root.val]
        while nodes:
            nsum = 0.0
            count = 0.0
            newnodes = []
            for node in nodes:
                if node.left:
                    newnodes.append(node.left)
                    nsum += node.left.val
                    count += 1.0
                if node.right:
                    newnodes.append(node.right)
                    nsum += node.right.val
                    count += 1.0
            nodes = newnodes
            if count > 0:
                avgs.append(nsum / count)

        return avgs
