from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_head, low_tail = None, None
        high_head, high_tail = None, None

        curr = head
        while curr:
            if curr.val < x:
                if not low_head:
                    low_head, low_tail = curr, curr
                else:
                    low_tail.next = curr
                    low_tail = curr
            else:
                if not high_head:
                    high_head, high_tail = curr, curr
                else:
                    high_tail.next = curr
                    high_tail = curr

            curr = curr.next

        if low_head:
            head = low_head
            low_tail.next = high_head
            if high_tail:
                high_tail.next = None
        else:
            head = high_head

        return head
