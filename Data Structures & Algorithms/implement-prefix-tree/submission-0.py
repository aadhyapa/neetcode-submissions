class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        currNode = self.trie
        for char in word:
            if char not in currNode.keys():
                currNode[char] = {}
            currNode = currNode[char]
        currNode[''] = {}

    def search(self, word: str) -> bool:
        currNode = self.trie

        for char in word:
            if char not in currNode.keys():
                return False
            currNode = currNode[char]

        # Checking if this is the end of the word
        if '' not in currNode.keys():
            return False

        return True

        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.trie

        for char in prefix:
            if char not in currNode.keys():
                return False
            currNode = currNode[char]

        return True
        