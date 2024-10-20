import unittest

from solution import Solution, Node


def get_connected_nodes(root):
    links = set()

    def search(node):
        if node:
            if node.next:
                links.add((node.val, node.next.val))
            else:
                links.add((node.val, None))
            search(node.left)
            search(node.right)

    search(root)
    return links


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        tree = Node(1,
                    left=Node(2,
                              left=Node(4),
                              right=Node(5)),
                    right=Node(3,
                               left=None,
                               right=Node(7)))
        output = Solution().connect2(tree)
        nexts = get_connected_nodes(output)
        self.assertEqual({
            (1, None),
            (2, 3), (3, None),
            (4, 5), (5, 7), (7, None),
        }, nexts)

    def test_case2(self):
        output = Solution().connect2(None)
        self.assertEqual(None, output)

    def test_case3(self):
        tree = Node(1,
                    left=Node(3),
                    right=Node(9,
                               left=Node(15),
                               right=Node(7)))
        output = Solution().connect2(tree)
        nexts = get_connected_nodes(output)
        self.assertEqual({
            (1, None),
            (3, 9), (9, None),
            (15, 7), (7, None),
        }, nexts)

    def test_case4(self):
        # [1,2,3,4,5,null,6,7,null,null,null,null,8]
        tree = Node(1,
                    left=Node(2,
                              left=Node(4,
                                        left=Node(7),
                                        right=None),
                              right=Node(5,
                                         left=None,
                                         right=None)),
                    right=Node(3,
                               left=None,
                               right=Node(6,
                                          left=None,
                                          right=Node(8))))
        output = Solution().connect2(tree)
        nexts = get_connected_nodes(output)
        self.assertEqual({
            (1, None),
            (2, 3), (3, None),
            (4, 5), (5, 6), (6, None),
            (7, 8), (8, None)
        }, nexts)

    def test_case5(self):
        # [2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
        tree = Node(2,
                    left=Node(1,
                              left=Node(0,
                                        left=Node(2,
                                                  left=None,
                                                  right=None),
                                        right=None),
                              right=Node(7,
                                         left=Node(1,
                                                   left=None,
                                                   right=None),
                                         right=Node(0,
                                                    left=Node(7)))),
                    right=Node(3,
                               left=Node(9,
                                         left=None,
                                         right=None),
                               right=Node(1,
                                          left=Node(8),
                                          right=Node(8))))
        output = Solution().connect2(tree)
        nexts = get_connected_nodes(output)
        self.assertEqual({
            (2, None),
            (1, 3), (3, None),
            (0, 7), (7, 9), (9, 1), (1, None),
            (2, 1), (1, 0), (0, 8), (8, 8), (8, None),
            (7, None),
        }, nexts)
