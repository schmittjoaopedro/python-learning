from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        half = n // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            nums1L = nums1[m1] if m1 >= 0 else float('-inf')
            nums1R = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('+inf')
            nums2L = nums2[m2] if m2 >= 0 else float('-inf')
            nums2R = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('+inf')

            if nums1L <= nums2R and nums2L <= nums1R:
                if n % 2:  # odd
                    return min(nums1R, nums2R)
                else:  # even
                    return (max(nums1L, nums2L) + min(nums1R, nums2R)) / 2
            elif nums1L > nums2R:
                r = m1 - 1
            else:
                l = m1 + 1
