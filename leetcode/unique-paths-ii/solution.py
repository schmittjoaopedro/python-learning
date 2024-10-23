from functools import cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def solve(r, c):
            if obstacleGrid[r][c] == 1:
                return 0
            if r == m - 1 and c == n - 1:  # Found target
                return 1

            paths = 0
            if r < m - 1:  # Can go down
                paths += solve(r + 1, c)
            if c < n - 1:  # Can go left
                paths += solve(r, c + 1)

            return paths

        return solve(0, 0)
