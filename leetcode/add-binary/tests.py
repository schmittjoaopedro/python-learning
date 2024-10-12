import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().addBinary("11", "1")
        self.assertEqual(output, "100")

    def test_case2(self):
        output = Solution().addBinary("1010", "1011")
        self.assertEqual(output, "10101")
