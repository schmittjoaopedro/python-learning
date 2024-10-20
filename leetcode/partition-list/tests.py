import unittest

from solution import Solution, ListNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        input = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
        output = Solution().partition(input, 3)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next.val, 2)
        self.assertEqual(output.next.next.val, 2)
        self.assertEqual(output.next.next.next.val, 4)
        self.assertEqual(output.next.next.next.next.val, 3)
        self.assertEqual(output.next.next.next.next.next.val, 5)
        self.assertEqual(output.next.next.next.next.next.next, None)

    def test_case2(self):
        input = ListNode(2, ListNode(1))
        output = Solution().partition(input, 2)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next.val, 2)
        self.assertEqual(output.next.next, None)

    def test_case3(self):
        output = Solution().partition(ListNode(1), 2)
        self.assertEqual(output.val, 1)
        self.assertEqual(output.next, None)
