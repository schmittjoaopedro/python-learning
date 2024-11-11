class Solution:
    def totalNQueens(self, n: int) -> int:
        usedCols, usedPosDiag, usedNegDiag = set(), set(), set()
        solutions = [0]

        def solve(r):
            if r == n:
                solutions[0] += 1
                return

            for c in range(n):
                if (c not in usedCols and
                        (r + c) not in usedPosDiag and
                        (r - c) not in usedNegDiag):
                    usedCols.add(c)
                    usedPosDiag.add(r + c)
                    usedNegDiag.add(r - c)
                    solve(r + 1)
                    usedNegDiag.remove(r - c)
                    usedPosDiag.remove(r + c)
                    usedCols.remove(c)

        solve(0)
        return solutions[0]
