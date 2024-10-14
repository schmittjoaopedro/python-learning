class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

        def solve(num):
            nsum = 0
            while num > 0:
                nsum += (num % 10) ** 2
                num = num // 10
            return nsum

        calculated = {n: True}
        while True:
            n = solve(n)
            if n == 1:
                return True
            if n in calculated:
                break
            calculated[n] = True

        return False
