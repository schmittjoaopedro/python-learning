from functools import cache
from math import inf
from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        dist = float('-inf')
        for i, n1 in enumerate(nums):
            currDist = n1
            dist = max(dist, currDist)
            for n2 in nums[i + 1:]:
                currDist += n2
                dist = max(dist, currDist)

        return dist

    def maxSubArray(self, nums: List[int]) -> int:
        # Uses Dynamic Programming to cache already computed values
        @cache
        def solve(i):
            if i == len(nums) - 1:
                return nums[i]
            s1 = nums[i]
            s2 = nums[i] + solve(i + 1)
            return max(s1, s2)

        maxN = -inf
        for i in range(0, len(nums)):
            maxN = max(maxN, solve(i))

        return maxN
