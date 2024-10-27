from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minheap = []
        res = []

        for i in range(min(k, len(nums1))):
            heappush(minheap, (
                nums1[i] + nums2[0],  # Combination sum
                0,  # Num2 index
                [nums1[i], nums2[0]]  # Combination elements
            ))

        for j in range(k):
            numSum, num2Idx, comb = heappop(minheap)
            res.append(comb)
            if num2Idx == len(nums2) - 1:
                continue
            nextIdx = num2Idx + 1
            heappush(minheap, (
                comb[0] + nums2[nextIdx],  # Combination sum
                nextIdx,  # Num2 index
                [comb[0], nums2[nextIdx]]  # Combination elements
            ))

        return res
