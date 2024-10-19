class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows == 1:
            return s

        rows_map = {i: '' for i in range(1, numRows + 1)}
        i = 1
        signal = 1
        rows_map[i] = s[0]
        for c in s[1:]:
            i += signal
            rows_map[i] += c
            if i == numRows:
                signal = -1
            elif i == 1:
                signal = 1

        word = ''
        for i in range(1, numRows + 1):
            word += rows_map[i]
        return word
