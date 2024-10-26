from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        visits = set()
        for node in graph.keys():
            if node in visits:
                continue
            if self.isThereCycle(graph, node, visits, set()):
                return False
        return True

    def isThereCycle(self, graph, node, visits, cycle):
        if node in cycle:
            return True
        if node in visits:
            return False
        visits.add(node)
        cycle.add(node)
        if node in graph:
            for dest in list(graph[node]):
                if self.isThereCycle(graph, dest, visits, cycle):
                    return True
        cycle.remove(node)
        return False

    def buildGraph(self, numCourses, prereqs):
        graph = {i: set() for i in range(numCourses)}
        for edge in prereqs:
            vdest, vsource = edge
            graph[vsource].add(vdest)
        return graph
