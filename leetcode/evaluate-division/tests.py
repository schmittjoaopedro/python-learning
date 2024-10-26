import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
                         Solution().calcEquation(
                             [["a", "b"], ["b", "c"]],
                             [2.0, 3.0],
                             [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
                         ))

    def test_case2(self):
        self.assertEqual([3.75000, 0.40000, 5.00000, 0.20000],
                         Solution().calcEquation(
                             [["a", "b"], ["b", "c"], ["bc", "cd"]],
                             [1.5, 2.5, 5.0],
                             [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
                         ))

    def test_case3(self):
        self.assertEqual([0.50000, 2.00000, -1.00000, -1.00000],
                         Solution().calcEquation(
                             [["a", "b"]],
                             [0.5],
                             [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
                         ))

    def test_case4(self):
        actual = Solution().calcEquation(
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
        )
        expected = [360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000]
        for exp, act in zip(expected, actual):
            self.assertAlmostEqual(exp, act, places=5)
