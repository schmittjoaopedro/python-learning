class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        5 = [0101] <- left
        6 = [0100]
        7 = [0111] <- right
        r = [0100]

        """
        if left == right:
            return left
        if abs(left - right) == 1:
            return left & right

        num = 0
        mask = 2 ** 32
        while mask > 0:
            leftMask = left & mask
            rightMask = right & mask
            if (leftMask > 0 or rightMask > 0) and not (leftMask > 0 and rightMask > 0):
                break
            if left & mask > 0 and right & mask > 0:
                num = num | mask
            mask = mask >> 1

        return num
