from functools import cache
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currIdx = 0
        farthestIdx = nums[0]

        while currIdx < len(nums) - 1:
            farthest = currIdx
            for i in range(currIdx + 1, min(farthestIdx + 1, len(nums))):
                if i + nums[i] >= farthest or i + nums[i] >= len(nums) - 1:
                    farthest = i + nums[i]
                    currIdx = i
            jumps += 1
            farthestIdx = currIdx + nums[currIdx]

        return jumps

    def jumpRec(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return len(nums) + 1

            maxjumps = min(nums[i], len(nums) - 1 - i) + 1
            return 1 + min([solve(i + j) for j in range(1, maxjumps)])

        return solve(0)
