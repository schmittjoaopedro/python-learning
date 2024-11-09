import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, Solution().calculate("1 + 1"))

    def test_case2(self):
        self.assertEqual(3, Solution().calculate(" 2-1 + 2 "))

    def test_case3(self):
        self.assertEqual(23, Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

    def test_case4(self):
        self.assertEqual(3, Solution().calculate("   (  3 ) "))

    def test_case5(self):
        self.assertEqual(3, Solution().calculate("1-(     -2)"))

    def test_case6(self):
        self.assertEqual(-12, Solution().calculate("- (3 + (4 + 5))"))
