import heapq
from queue import PriorityQueue
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap
        heap = nums[:k]
        heapq.heapify(heap)

        kth = heap[0]
        for n in nums[k:]:
            if n > kth:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
                kth = heap[0]

        return kth

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for n in nums:
            pri = -1.0*n
            pq.put((pri, n))

        kth = 0
        num = None
        while kth < k:
            num = pq.get()[1]
            kth += 1

        return num
