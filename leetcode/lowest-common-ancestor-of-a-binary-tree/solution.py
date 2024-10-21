class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        if not root:
            return None

        elems = {p.val, q.val}

        def search(node):
            if not node:
                return set(), None

            elLeft, ancLeft = search(node.left)
            if ancLeft is not None:
                return elLeft, ancLeft

            elRight, ancRight = search(node.right)
            if ancRight is not None:
                return elRight, ancRight

            allEls = elLeft.union(elRight)
            if node.val in elems:
                allEls.add(node.val)
            if allEls == elems:
                return allEls, node
            else:
                return allEls, None

        return search(root)[1]
