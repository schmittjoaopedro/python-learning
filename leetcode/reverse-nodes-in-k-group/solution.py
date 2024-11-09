from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = ListNode(0, head)
        s, f = self.findSF(dummy, k)
        while f:
            sn = s.next
            fn = f.next
            self.invert(sn, f)
            s.next = f
            sn.next = fn
            s, f = self.findSF(sn, k)

        return dummy.next

    def invert(self, start, end):
        curr = start
        prev = None
        while prev != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

    def findSF(self, node, k):
        s = f = node
        while k > 0:
            f = f.next
            if f is None:
                break
            k -= 1
        return s, f
