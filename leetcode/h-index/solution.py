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

    def hIndex2(self, citations: List[int]) -> int:
        n = len(citations)
        freqs = [0] * (n + 1) # To include a freq to 0

        for v in citations:
            freqs[min(n, v)] += 1

        i = n
        total = 0
        while i >= 0:
            total += freqs[i]
            if total >= i:
                return i
            i -= 1

        return 0