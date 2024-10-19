class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        for n in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                  (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                  (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
            while n[0] <= num:
                roman += n[1]
                num -= n[0]
        return roman

    def intToRoman2(self, num: int) -> str:
        # Process all thousands
        roman = ("M" * (num // 1000))
        num -= 1000 * (num // 1000)

        while num // 100 > 0:
            dig = num // 100
            if dig == 9:
                roman += "CM"
                num -= 900
            elif dig == 4:
                roman += "CD"
                num -= 400
            else:
                if dig >= 5:
                    roman += "D"
                    num -= 500
                else:
                    roman += "C"
                    num -= 100

        while num // 10 > 0:
            dig = num // 10
            if dig == 9:
                roman += "XC"
                num -= 90
            elif dig == 4:
                roman += "XL"
                num -= 40
            else:
                if dig >= 5:
                    roman += "L"
                    num -= 50
                else:
                    roman += "X"
                    num -= 10

        while num > 0:
            if num == 9:
                roman += "IX"
                num -= 9
            elif num == 4:
                roman += "IV"
                num -= 4
            else:
                if num >= 5:
                    roman += "V"
                    num -= 5
                else:
                    roman += "I"
                    num -= 1

        return roman
