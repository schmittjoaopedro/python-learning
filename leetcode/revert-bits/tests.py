import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().reverseBits(43261596)
        self.assertEqual(output, 964176192)

    def test_case2(self):
        output = Solution().reverseBits(4294967293)
        self.assertEqual(output, 3221225471)
