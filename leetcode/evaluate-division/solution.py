from typing import List


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqmap = self.getEqMapBase(equations, values)
        while self.createDependencies(eqmap):
            pass

        return self.resolveQueries(eqmap, queries)

    def resolveQueries(self, eqmap, queries):
        result = []
        for query in queries:
            if query[0] in eqmap and query[1] in eqmap[query[0]]:
                result.append(eqmap[query[0]][query[1]])
            else:
                result.append(-1)
        return result

    def createDependencies(self, eqmap):
        changed = False
        for v1 in list(eqmap.keys()):
            eqs1 = eqmap[v1]
            for v2 in list(eqs1.keys()):
                v1v2val = eqs1[v2]
                if v2 in eqmap:
                    for v3 in list(eqmap[v2].keys()):
                        v2v3val = eqmap[v2][v3]
                        if v1 != v3 and v3 not in eqs1:
                            eqs1[v3] = v1v2val * v2v3val
                            changed = True
        return changed

    def getEqMapBase(self, equations, values):
        eqmap = {}
        for i, eq in enumerate(equations):
            if eq[0] not in eqmap:
                eqmap[eq[0]] = {}
            if eq[1] not in eqmap:
                eqmap[eq[1]] = {}
            eqmap[eq[0]][eq[1]] = values[i]
            eqmap[eq[1]][eq[0]] = 1.0 / values[i]
            eqmap[eq[0]][eq[0]] = 1.0
            eqmap[eq[1]][eq[1]] = 1.0
        return eqmap
