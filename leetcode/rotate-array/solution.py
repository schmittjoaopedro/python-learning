from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        self.reverse(nums, 0, len(nums) - 1)
        k = k % len(nums)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, array, start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
