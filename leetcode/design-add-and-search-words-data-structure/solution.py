class WordDictionary:

    def __init__(self):
        self.vocab = {}

    def addWord(self, word: str) -> None:
        curr = self.vocab
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["_"] = True

    def search(self, word: str) -> bool:

        def find(i, options):
            if i == len(word):
                return "_" in options

            if word[i] == '.':
                if not options:
                    return False
                for k in options:
                    if k != '_' and find(i + 1, options[k]):
                        return True
            else:
                if word[i] in options:
                    if find(i + 1, options[word[i]]):
                        return True

            return False

        return find(0, self.vocab)
