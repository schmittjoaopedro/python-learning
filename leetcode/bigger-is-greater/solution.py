class Solution:

    def biggerIsGreater(self, word: str) -> str:
        chars = list(word)

        prevSmallest = len(chars) - 1
        for i in range(len(chars) - 2, -1, -1):
            if chars[i] < chars[i + 1]:
                prevSmallest = i
                break

        if prevSmallest == len(chars) - 1:
            return "no answer"
        else:
            nextBigger = prevSmallest + 1
            for j in range(nextBigger + 1, len(chars)):
                if chars[j] <= chars[nextBigger] and chars[j] > chars[prevSmallest]:
                    nextBigger = j

            chars[prevSmallest], chars[nextBigger] = chars[nextBigger], chars[prevSmallest]
            chars[prevSmallest + 1:] = list(reversed(chars[prevSmallest + 1:]))

            return "".join(chars)
