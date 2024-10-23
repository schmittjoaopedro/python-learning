from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        marked = set()

        def search(r, c):
            if board[r][c] == "X" or (r, c) in marked:
                return
            marked.add((r, c))

            if r > 0:
                search(r - 1, c)
            if r < m - 1:
                search(r + 1, c)
            if c > 0:
                search(r, c - 1)
            if c < n - 1:
                search(r, c + 1)

        for r in range(m):
            if (r, 0) not in marked:
                search(r, 0)
            if (r, n - 1) not in marked:
                search(r, n - 1)

        for c in range(n):
            if (0, c) not in marked:
                search(0, c)
            if (m - 1, c) not in marked:
                search(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r, c) not in marked:
                    board[r][c] = "X"
