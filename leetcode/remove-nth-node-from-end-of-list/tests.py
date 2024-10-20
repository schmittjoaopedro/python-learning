import unittest

from solution import Solution, ListNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().removeNthFromEnd(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next.val, 2)
        self.assertEqual(output.next.next.val, 3)
        self.assertEqual(output.next.next.next.val, 5)
        self.assertEqual(output.next.next.next.next, None)

    def test_case2(self):
        output = Solution().removeNthFromEnd(ListNode(1), 1)
        self.assertTrue(output is None)

    def test_case3(self):
        output = Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 1)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next, None)
