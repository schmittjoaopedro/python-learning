from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                count = self.countAroundAlive(board, r, c)
                if board[r][c] & 1:
                    if count < 2:
                        board[r][c] = board[r][c] & 0b01
                    elif 2 <= count <= 3:
                        board[r][c] = board[r][c] | 0b11
                    elif 3 < count:
                        board[r][c] = board[r][c] & 0b01
                elif count == 3:
                    board[r][c] = board[r][c] | 0b10

        for r in range(m):
            for c in range(n):
                board[r][c] = board[r][c] >> 1

    def countAroundAlive(self, board, r, c):
        count = 0
        if r - 1 >= 0:
            if c - 1 >= 0:
                count += board[r-1][c-1] & 0b1
            count += board[r-1][c] & 0b1
            if c + 1 < len(board[0]):
                count += board[r-1][c+1] & 0b1

        if c - 1 >= 0:
            count += board[r][c-1] & 0b1
        if c + 1 < len(board[0]):
            count += board[r][c+1] & 0b1

        if r + 1 < len(board):
            if c - 1 >= 0:
                count += board[r+1][c-1] & 0b1
            count += board[r+1][c] & 0b1
            if c + 1 < len(board[0]):
                count += board[r+1][c+1] & 0b1

        return count

    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dieCells = set()
        liveCells = set()
        for r in range(m):
            for c in range(n):
                count = self.countAroundAlive2(board, r, c)
                if board[r][c] == 1:
                    if count < 2:
                        dieCells.add((r, c))
                    elif 2 <= count <= 3:
                        liveCells.add((r, c))
                    elif 3 < count:
                        dieCells.add((r, c))
                elif count == 3:
                    liveCells.add((r, c))

        for cell in dieCells:
            r, c = cell
            board[r][c] = 0
        for cell in liveCells:
            r, c = cell
            board[r][c] = 1

    def countAroundAlive2(self, board, r, c):
        count = 0
        if r - 1 >= 0:
            if c - 1 >= 0:
                count += board[r - 1][c - 1]
            count += board[r - 1][c]
            if c + 1 < len(board[0]):
                count += board[r - 1][c + 1]

        if c - 1 >= 0:
            count += board[r][c - 1]
        if c + 1 < len(board[0]):
            count += board[r][c + 1]

        if r + 1 < len(board):
            if c - 1 >= 0:
                count += board[r + 1][c - 1]
            count += board[r + 1][c]
            if c + 1 < len(board[0]):
                count += board[r + 1][c + 1]

        return count
