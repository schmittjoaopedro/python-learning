from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = [root]
        curr = root.left
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        if self.hasNext():
            nextEl = self.stack.pop()

            if nextEl.right:
                self.stack.append(nextEl.right)
                curr = nextEl.right.left
                while curr:
                    self.stack.append(curr)
                    curr = curr.left

            return nextEl.val
        else:
            return -1

    def hasNext(self) -> bool:
        return len(self.stack) > 0
