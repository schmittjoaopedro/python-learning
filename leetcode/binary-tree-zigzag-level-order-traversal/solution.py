from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            result.append([n.val for n in queue])
            new_queue = []
            for node in queue[::-1]:
                if (len(result) - 1) % 2 == 0:
                    if node.right:
                        new_queue.append(node.right)
                    if node.left:
                        new_queue.append(node.left)
                else:
                    if node.left:
                        new_queue.append(node.left)
                    if node.right:
                        new_queue.append(node.right)

            queue = new_queue

        return result
