from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next

        array.sort()

        curr = head
        for val in array:
            curr.val = val
            curr = curr.next

        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def getMid(self, node):
        slow = node
        fast = node
        prev = node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev.next:
            prev.next = None
        return slow

    def merge(self, left, right):
        head = None
        curr = None
        if left.val < right.val:
            head, curr = left, left
            left = left.next
        else:
            head, curr = right, right
            right = right.next

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        while left:
            curr.next = left
            left = left.next
            curr = curr.next
        while right:
            curr.next = right
            right = right.next
            curr = curr.next

        return head
