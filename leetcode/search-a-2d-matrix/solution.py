from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.searchRow(matrix, target)
        if row < 0:
            return False
        col = self.searchCol(matrix[row], target)
        if col < 0:
            return False
        return True


    def searchRow(self, matrix, target):
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                return mid
            elif target < matrix[mid][0]:
                bottom = bottom - 1
            else:
                top = top + 1

        return -1

    def searchCol(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = right - 1
            else:
                left = left + 1

        return -1
