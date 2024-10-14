from functools import cache
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def solve(n):
            if n  == 0:
                return 1
            if n == 1:
                return solve(n-1)
            else:
                return solve(n-1) + solve(n-2)

        return solve(n)