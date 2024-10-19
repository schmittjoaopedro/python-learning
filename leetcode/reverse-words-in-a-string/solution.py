class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        result = ''
        left, right = n, n
        while left >= 0:
            left -= 1
            if s[left] == ' ' or left == -1:
                if right - left > 1:
                    if not len(result) == 0:
                        result += ' '
                    result += s[left+1:right]
                right = left

        return result
