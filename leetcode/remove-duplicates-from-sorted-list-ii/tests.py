import unittest

from solution import Solution, ListNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().deleteDuplicates(
            ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next.val, 2)
        self.assertEqual(output.next.next.val, 5)

    def test_case2(self):
        output = Solution().deleteDuplicates(
            ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))))
        self.assertEqual(output.val, 2)
        self.assertEqual(output.next.val, 3)
