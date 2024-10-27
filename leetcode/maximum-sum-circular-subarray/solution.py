from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, currMax, maxSum, currMin, minSum = 0, 0, nums[0], 0, nums[0]
        # Kadane’s Algorithm
        # Use Kadane's algorithm to sum the total of all array elements
        # then find the maxSubarray and minSubarray, but ignoring the circular aspect
        for i, n in enumerate(nums):
            currMax = max(currMax + n, n)
            maxSum = max(maxSum, currMax)
            currMin = min(currMin + n, n)
            minSum = min(minSum, currMin)
            total += n

        allNegatives = maxSum < 0
        if allNegatives:
            # If maxSum is less than zero, it means during the iterations we never
            # found any number greater than zero to assign max. So return the maxSum
            # which will actually point to the higher negative number
            return maxSum
        else:
            # Next we check for two conditions:
            # - If the maxSub array is not in the circular intersection,
            #   the maxSum will yield the higher value
            # - If the minSub array is not in the circular intersection,
            #   the minSum will yield the lower value. And for this case
            #   we can invert the calculation and return the difference
            #   of total and minSum.
            return max(maxSum, total - minSum)
