from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mnums = {n: i for i, n in enumerate(nums)}
        max_length = 0

        while mnums:
            num = next(iter(mnums))
            del mnums[num]
            length = 1

            temp = num - 1
            while temp in mnums:
                del mnums[temp]
                length += 1
                temp -= 1

            temp = num + 1
            while temp in mnums:
                del mnums[temp]
                length += 1
                temp += 1

            max_length = max(max_length, length)

        return max_length

    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        maxDist = 1
        prev = nums[0]
        count = 1
        for n in nums[1:]:
            if n - prev == 0:
                continue
            if n - prev == 1:
                count += 1
                maxDist = max(maxDist, count)
            else:
                count = 1
            prev = n

        return maxDist
