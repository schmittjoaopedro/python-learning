from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            if digit + carry > 9:
                digits[i] = (digit + carry) % 10
                carry = 1
            else:
                digits[i] = (digit + carry)
                carry = 0
        if carry:
            digits = [1] + digits
        return digits
