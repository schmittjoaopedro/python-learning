from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        graph = self.buildGraph([startGene, endGene, *bank])
        return self.solveByDFS(graph, startGene, endGene)

    def solveByDFS(self, graph, startGene, endGene):
        levels = 0
        queue = [startGene]
        visited = {startGene}
        while queue:
            levels += 1
            nextQueue = []
            for orig in queue:
                for dest in graph[orig]:
                    if dest == endGene:
                        return levels
                    if dest not in visited:
                        visited.add(dest)
                        nextQueue.append(dest)
            queue = nextQueue

        return -1

    def buildGraph(self, genes):
        graph = {g: set() for g in genes}
        for orig in genes:
            for dest in genes:
                if self.diffsCount(orig, dest) == 1:
                    graph[orig].add(dest)
        return graph

    def diffsCount(self, gene1, gene2):
        return sum([1 for i in range(len(gene1)) if gene1[i] != gene2[i]])
