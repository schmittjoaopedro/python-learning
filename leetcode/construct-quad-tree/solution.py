from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        # True if grid of 1's, False if grid of 0's, True or False if isLeaf is True
        self.val = val

        # False if node has 4 children
        # True if all 1's or all 0's children
        self.isLeaf = isLeaf

        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def checkEqual(self, grid):
        n = len(grid)
        base = grid[0][0]
        for r in range(n):
            for c in range(n):
                if grid[r][c] != base:
                    return False
        return True

    def splitGrid(self, grid):
        n = len(grid)
        half = n // 2
        grids = [[], [], [], []]
        for gi in range(4):
            if gi == 0:
                row_lower, row_upper, col_lower, col_upper = 0, half, 0, half
            elif gi == 1:
                row_lower, row_upper, col_lower, col_upper = 0, half, half, n
            elif gi == 2:
                row_lower, row_upper, col_lower, col_upper = half, n, 0, half
            else:
                row_lower, row_upper, col_lower, col_upper = half, n, half, n
            for r in range(row_lower, row_upper):
                grids[gi].append([])
                for c in range(col_lower, col_upper):
                    grids[gi][r - row_lower].append(grid[r][c])

        g1, g2, g3, g4 = grids
        return g1, g2, g3, g4

    def construct(self, grid: List[List[int]]) -> Node:
        val, isLeaf, topLeft, topRight, bottomLeft, bottomRight = None, None, None, None, None, None
        if self.checkEqual(grid):
            val = True if grid[0][0] == 1 else False
            isLeaf = True
        else:
            val = 1
            isLeaf = False
            g1, g2, g3, g4 = self.splitGrid(grid)
            topLeft = self.construct(g1)
            topRight = self.construct(g2)
            bottomLeft = self.construct(g3)
            bottomRight = self.construct(g4)

        return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
