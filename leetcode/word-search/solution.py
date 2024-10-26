from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        stack = set()

        def search(r, c, level):
            if level == len(word):
                return True

            # Go up
            if r > 0 and (r - 1, c) not in stack and board[r - 1][c] == word[level]:
                stack.add((r - 1, c))
                if search(r - 1, c, level + 1):
                    return True
                stack.remove((r - 1, c))

            # Go down
            if r < m - 1 and (r + 1, c) not in stack and board[r + 1][c] == word[level]:
                stack.add((r + 1, c))
                if search(r + 1, c, level + 1):
                    return True
                stack.remove((r + 1, c))

            # Go left
            if c > 0 and (r, c - 1) not in stack and board[r][c - 1] == word[level]:
                stack.add((r, c - 1))
                if search(r, c - 1, level + 1):
                    return True
                stack.remove((r, c - 1))

            # Go right
            if c < n - 1 and (r, c + 1) not in stack and board[r][c + 1] == word[level]:
                stack.add((r, c + 1))
                if search(r, c + 1, level + 1):
                    return True
                stack.remove((r, c + 1))

            return False

        for r in range(m):
            for c in range(n):
                if word[0] == board[r][c]:
                    stack.add((r, c))
                    if search(r, c, 1):
                        return True
                    stack.remove((r, c))

        return False