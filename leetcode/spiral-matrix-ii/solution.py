from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for i in range(n)]
        startRow, startCol, startNum, length = 0, 0, 1, n
        while length > 0:
            startNum = self.fillMatrixFrom(matrix, startRow, startCol, length, startNum)
            startRow += 1
            startCol += 1
            length = max(length - 2, 0)

        return matrix

    def fillMatrixFrom(self, matrix, startRow, startCol, length, startNum):
        if length == 1:
            matrix[startRow][startCol] = startNum
        else:
            # fill the top row from left to right
            for i in range(startCol, startCol + length):
                matrix[startRow][i] = startNum
                startNum += 1

            # fill the right column from to bottom (skip top and bottom rows)
            for i in range(startRow + 1, startRow + length - 1):
                matrix[i][startCol + length - 1] = startNum
                startNum += 1

            # fill the bottom row from right to left
            for i in reversed(range(startCol, startCol + length)):
                matrix[startRow + length - 1][i] = startNum
                startNum += 1

            # fill the left column from bottom to top (skip top and bottom rows)
            for i in reversed(range(startRow + 1, startRow + length - 1)):
                matrix[i][startCol] = startNum
                startNum += 1

        return startNum
