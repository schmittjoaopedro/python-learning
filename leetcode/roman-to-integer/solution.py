class Solution:

    def romanToInt(self, s: str) -> int:
        num = 0
        for letter in s[::-1]:
            if letter == "I":
                if num < 3:
                    num += 1
                else:
                    num -= 1
            elif letter == "V":
                num += 5
            elif letter == "X":
                if num < 30:
                    num += 10
                else:
                    num -= 10
            elif letter == "L":
                num += 50
            elif letter == "C":
                if num < 400:
                    num += 100
                else:
                    num -= 100
            elif letter == "D":
                num += 500
            else:
                num += 1000

        return num
        