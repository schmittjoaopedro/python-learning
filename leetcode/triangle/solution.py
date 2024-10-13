from functools import cache
from typing import List
from queue import PriorityQueue


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        @cache
        def solve(row, col, path):
            if row == len(triangle) - 1:
                cost, path = triangle[row][col], f"{triangle[row][col]}"
            else:
                leftCost, leftPath = solve(row + 1, col, path)
                rightCost, rightPath = solve(row + 1, col + 1, path)
                if leftCost < rightCost:
                    cost, path = triangle[row][col] + leftCost, f"{triangle[row][col]} -> {leftPath}"
                else:
                    cost, path = triangle[row][col] + rightCost, f"{triangle[row][col]} -> {rightPath}"

            return cost, path

        return solve(0, 0, "")

    # Dijkstra's algorithm doesn't work for this problem because there might
    # be negative weights.
    def minimumTotalDisjkstra(self, triangle: List[List[int]]) -> int:
        # Invert graph to make it easier to go from bottom to top
        inv_tri = triangle[::-1]

        vertices = {}
        for r in range(len(inv_tri)):
            for c in range(len(inv_tri[r])):
                vertices[(r, c)] = float("inf")

        edges = []
        for r in range(len(inv_tri)):
            for c in range(len(inv_tri[r])):
                if c > 0:
                    edges.append(((r, c), (r + 1, c - 1), inv_tri[r][c]))
                if c < len(inv_tri[r]) - 1:
                    edges.append(((r, c), (r + 1, c), inv_tri[r][c]))

        # Adjustment to finish the graph
        vertices[(len(inv_tri), 0)] = float("inf")
        edges.append(((len(inv_tri) - 1, 0), (len(inv_tri), 0), inv_tri[len(inv_tri) - 1][0]))

        for c in range(len(inv_tri[0])):
            vertices[(0, c)] = 0

        # Topological sort heuristic
        changes = False
        while changes:
            changes = False
            for u, v, w in edges:
                # Relaxation lemma
                if vertices[u] + w < vertices[v]:
                    vertices[v] = vertices[u] + w
                    changes = True

        # Dijkstra heuristic
        adj = {}
        for edge in edges:
            u, v, w = edge
            if u not in adj:
                adj[u] = {}
            adj[u][v] = w
        pq = PriorityQueue()
        for v in vertices.keys():
            if v[0] != len(inv_tri):
                pq.put((vertices[v], v))
            if v[0] == 0:
                pq.put((0, (0, v[0])))
        while pq.empty() is False:
            cost, u = pq.get()
            for v in adj[u]:
                w = adj[u][v]
                if vertices[u] + w < vertices[v]:
                    vertices[v] = vertices[u] + w

        return vertices[(len(inv_tri), 0)]
