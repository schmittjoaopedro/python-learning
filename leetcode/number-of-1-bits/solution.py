class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (n >> i) & 1:
                count += 1
        return count

    def hammingWeight2(self, n: int) -> int:
        nstr = bin(n)
        count = 0
        for c in nstr[2:]:  # ignore 0b prefix
            if c == "1":
                count += 1
        return count
