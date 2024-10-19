from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        nwords = len(words)
        wordsize = len(words[0])
        permsize = nwords * wordsize
        if len(s) < permsize:
            return []

        result = []
        prcmap = {w: (-1, 0) for w in words}
        refmap = {}
        for w in words:
            if w not in refmap:
                refmap[w] = 0
            refmap[w] += 1

        for i in range(len(s) - permsize + 1):
            count = 0
            while count < nwords:
                six = i + count * wordsize
                subw = s[six:six + wordsize]
                if subw not in prcmap:
                    break
                atp, cnt = prcmap[subw]
                if atp == i and cnt == refmap[subw]:
                    break
                if atp != i:
                    prcmap[subw] = (i, 1)
                else:
                    prcmap[subw] = (i, cnt + 1)
                count += 1
            if count == nwords:
                result.append(i)

        return result
