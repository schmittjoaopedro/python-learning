class Solution:
    def reverseBits1(self, n: int) -> int:
        nstr = bin(n)[2:]  # Remove 0b from the string
        nstr = nstr.rjust(32, '0')  # Append padding before reverting, int 32 bits
        nstr = nstr[::-1]
        return int(nstr, 2)

    def reverseBits(self, num: int) -> int:
        num = ((num & 0xffff0000) >> 16) | ((num & 0x0000ffff) << 16)
        num = ((num & 0xff00ff00) >> 8) | ((num & 0x00ff00ff) << 8)
        num = ((num & 0xf0f0f0f0) >> 4) | ((num & 0x0f0f0f0f) << 4)
        num = ((num & 0xcccccccc) >> 2) | ((num & 0x33333333) << 2)
        num = ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)
        return num
