from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return nums[0] == 0
        idx = 0
        while idx < len(nums):
            farIdx = 0
            biggestJump = 0
            for jidx, jsize in enumerate(nums[idx + 1:idx + 1 + nums[idx]]):
                jump = 1 + jidx + jsize
                if jump >= biggestJump:
                    farIdx = 1 + jidx
                    biggestJump = jump
            if farIdx == 0:
                break
            idx += farIdx

        return idx >= len(nums) - 1
