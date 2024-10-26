from collections import deque
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k:
            return []

        output = []
        q = deque()

        def solve(start, end):
            if len(q) == k:
                output.append(list(q))
                return

            for i in range(start, end + 1):
                q.append(i)
                solve(i + 1, end)
                q.pop()

        solve(1, n)

        return output
