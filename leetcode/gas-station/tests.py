import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(3, Solution().canCompleteCircuit(
            gas=[1, 2, 3, 4, 5],
            cost=[3, 4, 5, 1, 2]
        ))

    def test_case2(self):
        self.assertEqual(-1, Solution().canCompleteCircuit(
            gas=[2, 3, 4],
            cost=[3, 4, 3]
        ))
