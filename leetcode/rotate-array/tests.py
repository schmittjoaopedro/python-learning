import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        Solution().rotate(array, 3)
        self.assertEqual(array, [5, 6, 7, 1, 2, 3, 4])

    def test_case2(self):
        array = [-1, -100, 3, 99]
        Solution().rotate(array, 2)
        self.assertEqual(array, [3, 99, -1, -100])

    def test_case3(self):
        array = [-1, -100, 3, 99]
        Solution().rotate(array, 3)
        self.assertEqual(array, [-100, 3, 99, -1])
