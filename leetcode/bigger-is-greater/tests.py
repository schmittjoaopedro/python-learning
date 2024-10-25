import io
import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        with io.open("inputs.txt", "r") as f:
            inputs = f.readlines()
        with io.open("outputs.txt", "r") as f:
            expected = f.readlines()

        for i in range(len(inputs)):
            print(inputs[i].strip())
            self.assertEqual(expected[i].strip(), Solution().biggerIsGreater(inputs[i].strip()))

    def test_case2(self):
        self.assertEqual("wvokkqbmgbnwrbdlzwqfanzxtwiqasxgqnwvrlhwnhlhbxkx",
                         Solution().biggerIsGreater("wvokkqbmgbnwrbdlzwqfanzxtwiqasxgqnwvrlhwnhlhbkxx"))
