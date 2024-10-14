class Trie:

    def __init__(self):
        self.map = {}


    def insert(self, word: str) -> None:
        curr = self.map
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr["word"] = True


    def search(self, word: str) -> bool:
        curr = self.map
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return curr.get("word", False)


    def startsWith(self, prefix: str) -> bool:
        curr = self.map
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
