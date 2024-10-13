from functools import cache
from typing import List
from queue import PriorityQueue


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def solve(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]

            return min(triangle[row][col] + solve(row+1, col),
                       triangle[row][col] + solve(row+1, col+1))

        return solve(0, 0)

    # Dijkstra's algorithm doesn't work for this problem because there might
    # be negative weights.
    def minimumTotalDisjkstra(self, triangle: List[List[int]]) -> int:
        # Invert graph to make it easier to go from bottom to top
        graph = triangle[::-1]

        # Store tuples in format (cost, num, row, col)
        q = PriorityQueue()
        for i, el in enumerate(graph[0]):
            q.put((el, el, 0, i))

        curr = q.get()
        while curr[2] != len(triangle) - 1:
            cost, num, row, col = curr

            # Branch to right
            if col < len(graph[row]) - 1:
                nextNum = graph[row + 1][col]
                q.put((cost + nextNum, nextNum, row + 1, col))

            # Branch to left
            if col > 0:
                nextNum = graph[row + 1][col - 1]
                q.put((cost + nextNum, nextNum, row + 1, col - 1))

            curr = q.get()

        return curr[0]
