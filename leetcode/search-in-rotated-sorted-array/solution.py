from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        rotation = left
        left, right = rotation, (len(nums) - 1) + rotation

        while left <= right:
            mid = (left + right) // 2
            realmid = mid % len(nums)
            if nums[realmid] == target:
                return realmid
            if target < nums[realmid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search2(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            """
            Four cases:
            
            1) nums = [2,3,(4),5,1], target = 3
                3 and 4 are on the same side of 2
                3 is to left of 4
                go left
            
            2) nums = [2,3,(4),5,1], target = 5
                5 and 4 are on the same side of 2
                5 is to right of 4
                go right
            
            3) nums = [4,5,(1),2,3], target = 5
                1 and 5 are not on the same side of 4
                5 is bigger than 4
                go left

            4) nums = [3,4,(5),1,2], target = 1
                5 and 1 are not on the same side of 3
                1 is less than 3
                go right
            """
            sameSideOfLeftElement = (nums[middle] < nums[left]) == (target < nums[left])
            if sameSideOfLeftElement:
                if target < nums[middle]:
                    right = middle - 1  # Go left
                else:
                    left = middle + 1  # Go right
            else:
                if target >= nums[left]:
                    right = middle - 1  # Go left
                else:
                    left = middle + 1  # Go right

        return -1
