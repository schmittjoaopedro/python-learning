from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = deque()
        visited = [False] * len(nums)
        output = []

        def solve():
            if len(curr) == len(nums):
                output.append(list(curr))
            else:
                for i, n in enumerate(nums):
                    if not visited[i]:
                        visited[i] = True
                        curr.append(n)
                        solve()
                        curr.pop()
                        visited[i] = False

        solve()
        return output

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """
        This is more efficient but does not maintain the lexicographic order
        if the nums array is sorted. The method permute maintains the order.
        """
        result = []

        def solve(start):
            if start >= len(nums):
                result.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                solve(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        solve(0)
        return result
