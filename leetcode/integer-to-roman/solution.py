class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""

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