from typing import List


class Solution:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        output = []

        def solve(i, word):
            if i == len(digits):
                output.append(word)
                return

            for c in self.mapping[digits[i]]:
                solve(i + 1, word + c)

        solve(0, "")

        return output
