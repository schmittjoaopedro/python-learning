class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenght = max(len(a), len(b)) + 1
        a = a.zfill(lenght)
        b = b.zfill(lenght)
        c = ""

        carry = 0
        for i in reversed(range(0, lenght)):
            localSum = int(a[i]) + int(b[i]) + carry
            if localSum < 2:
                c = str(localSum) + c
                carry = 0
            elif localSum == 2:
                c = "0" + c
                carry = 1
            else:
                c = "1" + c
                carry = 1

        if c[0] == "0":
            c = c[1:]

        return c
