from typing import List


class Solution:

    def majorityElement1(self, nums: List[int]) -> int:
        res = majority = 0

        for n in nums:
            if majority == 0:
                res = n

            majority += 1 if n == res else -1

        return res

    def majorityElement2(self, nums: List[int]) -> int:
        counts: dict = {}
        majority = int(len(nums) / 2)
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            if counts[num] > majority:
                return num

        raise Exception("Invalid nums array")

    def majorityElement3(self, nums: List[int]) -> int:
        majority = int(len(nums) / 2)
        nums.sort()
        count = 0
        prev = None
        for num in nums:
            if num == prev or prev is None:
                count += 1
                if count > majority:
                    return num
            else:
                count = 1
                prev = num
        raise Exception("Invalid nums array")
