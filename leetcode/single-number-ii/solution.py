from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1, x2, mask = 0, 0, 0

        for i in nums:
            x2 = x2 ^ (x1 & i)
            x1 = x1 ^ i
            mask = ~(x1 & x2)
            x2 = x2 & mask
            x1 = x1 & mask

        return x1
