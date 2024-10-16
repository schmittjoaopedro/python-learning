import heapq
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hmax = 0
        for i in range(len(citations) - 1, -1, -1):
            pappers = len(citations) - i
            if citations[i] <= pappers:
                hmax = max(hmax, citations[i])
                break
            elif citations[i] >= pappers:
                hmax = max(hmax, pappers)

        return hmax
