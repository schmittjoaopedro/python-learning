from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mnums = {n:i for i,n in enumerate(nums)}
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
