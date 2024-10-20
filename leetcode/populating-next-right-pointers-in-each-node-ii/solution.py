class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None

        def link(node):
            if node.left and node.right:
                node.left.next = node.right

            nextNode = node.next
            leftMost = None
            while nextNode and not leftMost:
                leftMost = nextNode.left or nextNode.right
                nextNode = nextNode.next
            if leftMost:
                if node.right:
                    node.right.next = leftMost
                elif node.left:
                    node.left.next = leftMost

            if node.right:
                link(node.right)
            if node.left:
                link(node.left)

        link(root)
        return root

    def connect2(self, root):
        if not root:
            return None

        queue = [root]
        while queue:
            for i in range(len(queue)):
                if i < len(queue) - 1:
                    queue[i].next = queue[i + 1]
            nextLevel = []
            for el in queue:
                if el.left:
                    nextLevel.append(el.left)
                if el.right:
                    nextLevel.append(el.right)
            queue = nextLevel

        return root
