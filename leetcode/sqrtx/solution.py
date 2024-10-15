class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = (x // 2) + 1
        while left <= right:
            base = left + (right - left) // 2
            if base == x // base:
                return base
            elif base > x // base:
                right = base - 1
            else:
                left = base + 1
        return right
