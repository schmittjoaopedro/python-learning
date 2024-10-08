from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # [1,2,2,2,null,2]
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        left_tree = self.deepSearch([], root.left)
        right_tree = self.deepSearch([], root.right)
        if len(left_tree) != len(right_tree):
            return False

        for i in range(0, len(left_tree)):
            if left_tree[i] != right_tree[len(right_tree) - 1 - i]:
                return False

        return True

    def deepSearch(self, t_list, curr, level=0):
        if curr.left:
            self.deepSearch(t_list, curr.left, level + 1)

        t_list.append(f"{curr.val}-{level}")

        if curr.right:
            self.deepSearch(t_list, curr.right, level + 1)
        return t_list


class Solution2:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        q_left = deque()
        q_right = deque()
        q_left.append(root.left)
        q_right.append(root.right)
        while len(q_left) > 0 and len(q_right) > 0:
            c_left = q_left.popleft()
            c_right = q_right.popleft()
            if c_left and c_right:
                if c_left.val != c_right.val:
                    return False
                q_left.append(c_left.left)
                q_left.append(c_left.right)
                q_right.append(c_right.right)
                q_right.append(c_right.left)
            elif c_left != None or c_right != None:
                return False

        return len(q_left) == 0 and len(q_right) == 0
