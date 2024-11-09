import unittest

from solution import Solution, ListNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        head = Solution().reverseKGroup(head, 2)
        self.assertEqual(head.val, 2)
        self.assertEqual(head.next.val, 1)
        self.assertEqual(head.next.next.val, 4)
        self.assertEqual(head.next.next.next.val, 3)
        self.assertEqual(head.next.next.next.next.val, 5)

    def test_case2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        head = Solution().reverseKGroup(head, 3)
        self.assertEqual(head.val, 3)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 1)
        self.assertEqual(head.next.next.next.val, 4)
        self.assertEqual(head.next.next.next.next.val, 5)
