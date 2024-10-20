import unittest

from solution import Solution, ListNode


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        output = Solution().rotateRight(input, 2)
        self.assertEqual(output.val, 4)
        self.assertEqual(output.next.val, 5)
        self.assertEqual(output.next.next.val, 1)
        self.assertEqual(output.next.next.next.val, 2)
        self.assertEqual(output.next.next.next.next.val, 3)
        self.assertEqual(output.next.next.next.next.next, None)

    def test_case2(self):
        input = ListNode(0, ListNode(1, ListNode(2)))
        output = Solution().rotateRight(input, 4)
        self.assertEqual(output.val, 2)
        self.assertEqual(output.next.val, 0)
        self.assertEqual(output.next.next.val, 1)
        self.assertEqual(output.next.next.next, None)

    def test_case3(self):
        output = Solution().rotateRight(None, 1)
        self.assertEqual(output, None)

    def test_case4(self):
        input = ListNode(1, ListNode(2, ListNode(3)))
        output = Solution().rotateRight(input, 2000000000)
        self.assertEqual(output.val, 2)
        self.assertEqual(output.next.val, 3)
        self.assertEqual(output.next.next.val, 1)
        self.assertEqual(output.next.next.next, None)
