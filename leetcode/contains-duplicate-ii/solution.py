from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        for i, num in enumerate(nums):
            if num in mem:
                if (i - mem[num]) <= k:
                    return True
            mem[num] = i

        return False
