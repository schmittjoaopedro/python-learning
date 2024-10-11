import unittest

from solution import Solution, ListNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        output = Solution().sortList(head)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next.val, 2)
        self.assertEqual(output.next.next.val, 3)
        self.assertEqual(output.next.next.next.val, 4)

    def test_case2(self):
        head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
        output = Solution().sortList(head)
        self.assertEqual(output.val, -1)
        self.assertEqual(output.next.val, 0)
        self.assertEqual(output.next.next.val, 3)
        self.assertEqual(output.next.next.next.val, 4)
        self.assertEqual(output.next.next.next.next.val, 5)

    def test_case3(self):
        output = Solution().sortList(None)
        self.assertEqual(output, None)

    def test_case4(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        output = Solution().sortList(head)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next.val, 2)
        self.assertEqual(output.next.next.val, 3)
        self.assertEqual(output.next.next.next.val, 4)
