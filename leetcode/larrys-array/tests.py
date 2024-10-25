import io
import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        inputs = []
        outputs = []
        with io.open("inputs.txt", "r") as f:
            line = int(f.readline())
            for i in range(line):
                f.readline()
                inputs.append(list(map(int, f.readline().split())))
        with io.open("outputs.txt", "r") as f:
            allLines = f.readlines()
            for line in allLines:
                outputs.append(line.strip())

        for i in range(len(inputs)):
            self.assertEqual(outputs[i], Solution().larrysArrayBruteForce(inputs[i]))

    def test_case2(self):
        # self.assertEqual("YES", Solution().larrysArrayBruteForce([3, 1, 2]))
        self.assertEqual("YES", Solution().larrysArrayBruteForce([1, 3, 4, 2]))
        # self.assertEqual("NO", Solution().larrysArrayBruteForce([1, 2, 3, 5, 4]))

    def test_case3(self):
        self.assertEqual("NO", Solution().larrysArrayBruteForce([1, 6, 5, 2, 3, 4]))
        self.assertEqual("YES", Solution().larrysArrayBruteForce([3, 1, 2, 4]))
