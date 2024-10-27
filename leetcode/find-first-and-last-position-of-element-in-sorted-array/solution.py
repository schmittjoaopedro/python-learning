from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minIdx = self.searchMin(nums, target)
        maxIdx = self.searchMax(nums, target)
        if minIdx is None or maxIdx is None:
            return [-1, -1]
        else:
            return [minIdx, maxIdx]

    def searchMax(self, nums, target):
        left, right = 0, len(nums) - 1
        maxIdx = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                maxIdx = max(maxIdx, mid)
                left = mid + 1
                continue

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return maxIdx if maxIdx > -1 else None

    def searchMin(self, nums, target):
        left, right = 0, len(nums) - 1
        minIdx = len(nums) + 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                minIdx = min(minIdx, mid)
                right = mid - 1
                continue

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return minIdx if minIdx < len(nums) else None
