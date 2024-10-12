class Solution:
    def reverseBits(self, n: int) -> int:
        nstr = bin(n)[2:]  # Remove 0b from the string
        nstr = nstr.rjust(32, '0')  # Append padding before reverting, int 32 bits
        nstr = nstr[::-1]
        return int(nstr, 2)
