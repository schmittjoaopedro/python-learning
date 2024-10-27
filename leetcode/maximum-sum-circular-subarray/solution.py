from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, currMax, maxSum, currMin, minSum = 0, 0, nums[0], 0, nums[0]
        for n in nums:
            currMax = max(currMax + n, n)
            maxSum = max(maxSum, currMax)
            currMin = min(currMin + n, n)
            minSum = min(minSum, currMin)
            total += n

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
