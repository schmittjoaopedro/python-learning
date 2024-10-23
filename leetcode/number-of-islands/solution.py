from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])

        def search(r, c):
            if grid[r][c] == "0" or (r, c) in seen:
                return
            else:
                seen.add((r, c))

            if r > 0:  # Move up
                search(r - 1, c)
            if r < m - 1:  # Move down
                search(r + 1, c)
            if c > 0:  # Move left
                search(r, c - 1)
            if c < n - 1:  # Move right
                search(r, c + 1)

        islands = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in seen and grid[r][c] != "0":
                    search(r, c)
                    islands += 1

        return islands
