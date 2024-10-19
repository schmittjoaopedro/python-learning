import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual("PAHNAPLSIIGYIR", Solution().convert("PAYPALISHIRING", 3))

    def test_case2(self):
        self.assertEqual("PINALSIGYAHRPI", Solution().convert("PAYPALISHIRING", 4))

    def test_case3(self):
        self.assertEqual("A", Solution().convert("A", 1))

    def test_case4(self):
        self.assertEqual("AB", Solution().convert("AB", 1))
