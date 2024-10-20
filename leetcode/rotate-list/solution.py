from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        k = k % length
        if k == 0:
            return head

        slow, fast = head, head
        dist = 0
        while dist < k:
            fast = fast.next
            dist += 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None

        return head
