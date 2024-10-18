from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        n = len(gas)
        i = 0
        start = 0
        balance = 0
        tries = n
        while True:
            idx = i % n
            if balance + gas[idx] >= cost[idx]:
                if i - start == n:
                    return start
                balance = balance + gas[idx] - cost[idx]
                i += 1
            else:
                balance = 0
                i += 1
                start = i
                tries -= 1
                if tries == 0:
                    return -1
