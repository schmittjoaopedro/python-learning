class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        vocab = self.getVocab(t)
        count = len(t)
        head, start, dist = 0, 0, len(s) + 1

        for end, c in enumerate(s):
            if c in vocab:
                if vocab[c] > 0:
                    count -= 1
                vocab[c] -= 1

            while count == 0:
                if end - start < dist:
                    head = start
                    dist = end - start

                if s[start] in vocab:
                    vocab[s[start]] += 1
                    if vocab[s[start]] > 0:
                        count += 1
                start += 1

        return "" if dist > len(s) else s[head:head + dist + 1]

    def getVocab(self, word):
        smap = {}
        for c in word:
            if c not in smap:
                smap[c] = 0
            smap[c] += 1
        return smap
