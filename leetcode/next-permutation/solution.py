from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        break_point = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_point = i
                break

        if break_point == -1:
            self.reverse(nums, 0)
        else:
            greatest_idx = -1
            for i in range(n - 1, -1, -1):
                if nums[i] > nums[break_point]:
                    greatest_idx = i
                    break

            nums[break_point], nums[greatest_idx] = nums[greatest_idx], nums[break_point]
            self.reverse(nums, break_point + 1)

    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def findNetworkCalls(self, reviews, counts):
        if not reviews or not counts:
            return []

        networkCalls = []
        for count in counts:
            total = 0
            for rev in reviews:
                total += abs(rev - count)
            networkCalls.append(total)

        return networkCalls

    def nextSpecialString(self, s: str) -> str:
        n = len(s)
        chars = list(s)

        if n == 1 and s == 'z':
            return "-1"
        if chars[0] == 'z' and chars[1] == 'z':
            return "-1"

        for i in range(n - 1, -1, -1):
            if chars[i] == 'z':
                chars[i] = 'a'
            else:
                chars[i] = chr(ord(chars[i]) + 1)
                break

        charsPrev = ['-'] + chars[:n-1]
        found = False
        for i in range(n):
            if found:
                if chars[i-1] != 'a':
                    chars[i] = 'a'
                else:
                    chars[i] = 'b'
            if chars[i] == charsPrev[i]:
                chars[i] = chr(ord(chars[i]) + 1)
                found = True

        return "".join(chars)
