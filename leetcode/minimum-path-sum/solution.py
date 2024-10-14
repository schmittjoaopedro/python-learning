from functools import cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @cache
        def solve(r, c):
            num = grid[r][c]

            # Base case, bottom right cell
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return num

            down = float('inf')
            right = float('inf')
            if r < len(grid) - 1:
                down = num + solve(r+1, c)
            if c < len(grid[0]) - 1:
                right = num + solve(r, c+1)

            return min(down, right)

        return solve(0, 0)

