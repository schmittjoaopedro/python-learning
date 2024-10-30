class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        def solve(power):
            if power == 1:
                return x

            half = power // 2
            res = solve(half)
            if 2 * half == power:
                return res * res
            else:
                return x * res * res

        return solve(n) if n > 0 else 1.0 / solve(n * -1)
