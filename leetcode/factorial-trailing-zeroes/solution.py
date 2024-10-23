class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        powerOfFive = 5

        while n // powerOfFive:
            zeros += n // powerOfFive
            powerOfFive *= 5

        return zeros
