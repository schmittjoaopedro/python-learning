from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        word = strs[0]
        otherWords = strs[1:]
        while True:
            ok = True
            if i < len(word):
                for word2 in otherWords:
                    if i == len(word2) or word[i] != word2[i]:
                        ok = False
            else:
                ok = False

            if ok:
                prefix += word[i]
                i += 1
            else:
                break

        return prefix
