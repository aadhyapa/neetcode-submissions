class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.Trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        currNode = self.Trie
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.end = True

    def search(self, word: str) -> bool:

        def searchHelper(charIndex, trieNode):


            if charIndex == len(word):
                return trieNode.end

            char = word[charIndex]

            verdict = False
            if char == '.':
                
                for node in trieNode.children.values():
                    verdict = (verdict or searchHelper(charIndex + 1, node))
                return verdict

            # Checking match
            if char not in trieNode.children:
                return False

            # Progressig
            return searchHelper(charIndex + 1, trieNode.children[char])


        return searchHelper(0, self.Trie)
        
