from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = self.buildGraph(wordList + [beginWord, endWord])

        currLevel = [beginWord]
        visit = set()
        levels = 1
        while currLevel:
            nextLevel = []
            levels += 1
            for s in currLevel:
                visit.add(s)
                for e in graph[s]:
                    if e == endWord:
                        return levels
                    if e not in visit:
                        nextLevel.append(e)
            currLevel = nextLevel

        return 0

    def buildGraph(self, words):
        graph = defaultdict(set)
        for i, w1 in enumerate(words):
            for w2 in words[i + 1:]:
                if self.areAdjacent(w1, w2):
                    graph[w1].add(w2)
                    graph[w2].add(w1)

        return graph

    def areAdjacent(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
            if diff > 1:
                return False

        return True
