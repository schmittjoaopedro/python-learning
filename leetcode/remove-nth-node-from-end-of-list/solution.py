from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        llmap = {}
        curr = head
        i = 0
        while curr:
            i += 1
            llmap[i] = curr
            curr = curr.next

        if n - i == 0:
            return head.next

        prevToRemove = llmap[i - n]
        prevToRemove.next = prevToRemove.next.next

        return head
