import unittest

from solution import Solution


class SolutionTest(unittest.TestCase):

    def test_case1(self):
        self.assertEqual([
            "This    is    an",
            "example  of text",
            "justification.  "],
            Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

    def test_case2(self):
        self.assertEqual(["What   must   be",
                          "acknowledgment  ",
                          "shall be        "],
                         Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))

    def test_case3(self):
        self.assertEqual(["Science  is  what we",
                          "understand      well",
                          "enough to explain to",
                          "a  computer.  Art is",
                          "everything  else  we",
                          "do                  "],
                         Solution().fullJustify(
                             ["Science", "is", "what", "we", "understand", "well",
                              "enough", "to", "explain", "to", "a", "computer.",
                              "Art", "is", "everything", "else", "we", "do"], 20))
