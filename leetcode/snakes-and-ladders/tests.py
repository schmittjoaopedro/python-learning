import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        output = Solution().snakesAndLadders([[-1, -1, -1, -1, -1, -1],
                                              [-1, -1, -1, -1, -1, -1],
                                              [-1, -1, -1, -1, -1, -1],
                                              [-1, 35, -1, -1, 13, -1],
                                              [-1, -1, -1, -1, -1, -1],
                                              [-1, 15, -1, -1, -1, -1]])
        self.assertEqual(output, 4)

    def test_case2(self):
        output = Solution().snakesAndLadders([[-1, -1],
                                              [-1, 3]])
        self.assertEqual(output, 1)

    def test_case3(self):
        output = Solution().snakesAndLadders([[1, 1, -1],
                                              [1, 1, 1],
                                              [-1, 1, 1]])
        self.assertEqual(output, -1)

    def test_case4(self):
        output = Solution().snakesAndLadders([[-1, 1, 2, -1],
                                              [2, 13, 15, -1],
                                              [-1, 10, -1, -1],
                                              [-1, 6, 2, 8]])
        self.assertEqual(output, 2)

    def test_case5(self):
        output = Solution().snakesAndLadders([[-1, 4, -1],
                                              [6, 2, 6],
                                              [-1, 3, -1]])
        self.assertEqual(output, 2)

    def test_case6(self):
        output = Solution().snakesAndLadders([[-1, 15, 9, 1, -1],
                                              [-1, -1, 10, 5, 19],
                                              [18, -1, 23, 9, -1],
                                              [1, 13, -1, 16, 20],
                                              [-1, 10, 10, 25, 13]])
        self.assertEqual(output, 1)

    def test_case7(self):
        output = Solution().snakesAndLadders([[-1, -1, 30, 14, 15, -1],
                                              [23, 9, -1, -1, -1, 9],
                                              [12, 5, 7, 24, -1, 30],
                                              [10, -1, -1, -1, 25, 17],
                                              [32, -1, 28, -1, -1, 32],
                                              [-1, -1, 23, -1, 13, 19]])
        self.assertEqual(output, 2)
