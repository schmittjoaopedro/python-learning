class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstOcurr = -1

        if len(needle) <= len(haystack):
            i = 0
            while i <= len(haystack) - len(needle):
                if haystack[i:i+len(needle)] == needle:
                    firstOcurr = i
                    break
                i += 1

        return firstOcurr