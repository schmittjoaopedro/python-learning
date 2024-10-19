from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        doc = self.get_doc(words, maxWidth)

        justified = []
        for i in range(len(doc) - 1):
            justified.append(self.justify_row(doc[i], maxWidth))

        last_sentence = " ".join(doc[-1])
        last_sentence += " " * (maxWidth - len(last_sentence))
        justified.append(last_sentence)

        return justified

    def justify_row(self, row, maxWidth):
        words = len(row)
        letters = sum([len(w) for w in row])
        spaces = words - 1
        if spaces == 0:
            return row[0] + (" " * (maxWidth - letters))

        spread = (maxWidth - letters) / spaces
        sentence = row[0]
        base_size = int(spread)
        remaining = maxWidth - letters - base_size * spaces
        for word in row[1:]:
            size = base_size if remaining == 0 else base_size + 1
            remaining = max(0, remaining - 1)
            sentence += (" " * size) + word
        return sentence

    def get_doc(self, words, maxWidth):
        doc = [[]]
        count = 0
        for word in words:
            space = 1 if doc[-1] else 0
            if count + space + len(word) > maxWidth:
                doc.append([])
                space, count = 0, 0
            doc[-1].append(word)
            count += len(word) + space
        return doc
