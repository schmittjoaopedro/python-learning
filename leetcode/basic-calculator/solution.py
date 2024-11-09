class Solution:
    def calculate(self, s: str) -> int:
        num, sign, res = 0, 1, 0
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '-+':
                res += num * sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append((res, sign))
                res, sign = 0, 1
            elif c == ')':
                endCalc = res + sign * num
                pres, psign = stack.pop()
                res = pres + psign * endCalc
                num = 0
        return res + num * sign
