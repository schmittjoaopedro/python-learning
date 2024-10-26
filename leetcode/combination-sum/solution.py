from collections import deque
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        curr = deque()

        def solve(start, tsum):
            if tsum == target:
                combs.append(list(curr))
                return
            if tsum > target:
                return
            for i, n in enumerate(candidates):
                if i >= start:
                    curr.append(n)
                    solve(i, tsum + n)
                    curr.pop()

        solve(0, 0)
        return combs