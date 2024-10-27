from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if self.isMin(nums, mid):
                return nums[mid]

            if nums[left] > nums[right] and nums[mid] > nums[right]:
                left = mid + 1  # Go right
            else:
                right = mid - 1  # Go left

    def isMin(self, nums, idx):
        leftVal, rightVal = nums[idx] + 1, nums[idx] + 1
        if idx > 0:
            leftVal = nums[idx - 1]
        if idx < len(nums) - 1:
            rightVal = nums[idx + 1]
        return leftVal > nums[idx] < rightVal
