from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if self.isPeak(nums, start):
                return start
            elif self.isPeak(nums, end):
                return end
            elif self.isPeak(nums, middle):
                return middle

            if nums[middle-1] > nums[middle]:
                end = middle - 1
            else:
                start = middle + 1

    def isPeak(self, nums, index):
        left, right = float("-inf"), float("-inf")
        if index > 0:
            left = nums[index - 1]
        if index < len(nums) - 1:
            right = nums[index + 1]
        return left < nums[index] > right
