from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, incCount = self.buildGraph(numCourses, prerequisites)
        return self.solveByBFS(graph, incCount)
        # return self.solveByDFS(graph)

    def solveByBFS(self, graph, incCount):
        # Create a start queue with all nodes with no incoming edges
        queue = deque()
        for i in range(len(incCount)):
            if incCount[i] == 0:
                queue.append(i)

        # Visit all nodes via BFS, starting from the nodes without
        # incoming edges. Every time a new node is visited the last
        # time, meaning all their incoming edges were consumed, add
        # it as the next element in the 'order' array
        visited = 0
        order = []
        while queue:
            orig = queue.popleft()
            order.append(orig)
            for dest in graph[orig]:
                incCount[dest] -= 1
                if incCount[dest] == 0:
                    queue.append(dest)

        return order if len(order) == len(incCount) else []

    def solveByDFS(self, graph):
        visited = set()
        onStack = set()
        order = []

        def hasOrder(orig):
            visited.add(orig)
            onStack.add(orig)
            for dest in graph[orig]:
                if dest not in visited:
                    if not hasOrder(dest):
                        return False
                elif dest in onStack:
                    return False
            onStack.remove(orig)
            order.append(orig)
            return True

        for node in graph.keys():
            if node not in visited and not hasOrder(node):
                return []

        return list(reversed(order))

    def buildGraph(self, numCourses, prereqs):
        graph = {i: set() for i in range(numCourses)}
        incCount = [0] * numCourses
        for edge in prereqs:
            dest, orig = edge
            incCount[dest] += 1
            graph[orig].add(dest)
        return graph, incCount
