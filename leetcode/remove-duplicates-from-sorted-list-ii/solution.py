from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def safe(curr):
            if not curr or not curr.next:
                return True
            if not curr.next.next:
                return curr.val != curr.next.val
            else:
                return curr.val != curr.next.val and curr.next.val != curr.next.next.val

        dummy = ListNode(val=None, next=head)
        prev = dummy
        curr = dummy
        while curr:
            if safe(curr):
                curr = curr.next
                prev.next = curr
                prev = curr
            else:
                curr = curr.next

        return dummy.next
