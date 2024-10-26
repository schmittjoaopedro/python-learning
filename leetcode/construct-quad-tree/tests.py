import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        root = Solution().construct([
            [0, 1],
            [1, 0],
        ])
        self.assertEqual(False, root.isLeaf)
        self.assertEqual(1, root.val)
        self.assertEqual(True, root.topLeft.isLeaf)
        self.assertEqual(0, root.topLeft.val)
        self.assertEqual(True, root.topRight.isLeaf)
        self.assertEqual(1, root.topRight.val)
        self.assertEqual(True, root.bottomLeft.isLeaf)
        self.assertEqual(1, root.bottomLeft.val)
        self.assertEqual(True, root.bottomRight.isLeaf)
        self.assertEqual(0, root.bottomRight.val)

    def test_case2(self):
        root = Solution().construct([
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ])
        self.assertEqual(False, root.isLeaf)
        self.assertEqual(1, root.val)
        self.assertEqual(True, root.topLeft.isLeaf)
        self.assertEqual(1, root.topLeft.val)
        self.assertEqual(False, root.topRight.isLeaf)
        self.assertEqual(1, root.topRight.val)
        self.assertEqual(True, root.bottomLeft.isLeaf)
        self.assertEqual(1, root.bottomLeft.val)
        self.assertEqual(True, root.bottomRight.isLeaf)
        self.assertEqual(0, root.bottomRight.val)
        self.assertEqual(True, root.topRight.topLeft.isLeaf)
        self.assertEqual(0, root.topRight.topLeft.val)
        self.assertEqual(True, root.topRight.topRight.isLeaf)
        self.assertEqual(0, root.topRight.topRight.val)
        self.assertEqual(True, root.topRight.bottomLeft.isLeaf)
        self.assertEqual(1, root.topRight.bottomLeft.val)
        self.assertEqual(True, root.topRight.bottomRight.isLeaf)
        self.assertEqual(1, root.topRight.bottomRight.val)
