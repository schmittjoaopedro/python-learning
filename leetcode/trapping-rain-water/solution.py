from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = height[0], height[n - 1]
        water = 0
        leftIdx, rightIdx = 0, n - 1

        while leftIdx < rightIdx:
            if leftMax <= rightMax:
                leftIdx += 1
                water += max(0, leftMax - height[leftIdx])
                leftMax = max(leftMax, height[leftIdx])
            else:
                rightIdx -= 1
                water += max(0, rightMax - height[rightIdx])
                rightMax = max(rightMax, height[rightIdx])

        return water
