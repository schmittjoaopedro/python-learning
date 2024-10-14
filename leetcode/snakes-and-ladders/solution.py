from typing import List
import collections


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        seen = set()
        queue = collections.deque()
        queue.append((1, 0, ""))
        while queue:
            label, step, path = queue.popleft()
            r, c = self.idxToRowCol(label, n)
            if board[r][c] != -1:
                label = board[r][c]
            if label == n * n:
                print(path)
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n * n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step + 1, f"{path} -> {label} -> {new_label}"))
        return -1

    def idxToRowCol(self, idx, n):
        if n % 2 == 0:
            row = n - 1 - ((idx - 1) // n)
            col = (idx - 1) % n
            col = col if row % 2 != 0 else n - 1 - col
        else:
            row = n - 1 - ((idx - 1) // n)
            col = (idx - 1) % n
            col = col if row % 2 == 0 else n - 1 - col
        return row, col
