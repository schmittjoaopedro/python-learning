from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        cols = set()
        for r in range(n):
            zeroed = False
            for c in range(m):
                if matrix[r][c] == 0:
                    cols.add(c)
                    zeroed = True
            if zeroed:
                matrix[r] = [0] * m

        for c in cols:
            for r in range(n):
                matrix[r][c] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        cols, rows = set(), set()
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            for c in range(m):
                matrix[r][c] = 0

        for c in cols:
            for r in range(n):
                matrix[r][c] = 0
