class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.found = False
        self.word = ''

class Trie:
    def __init__(self):
        self.wordTrie = TrieNode()

    def addWord(self, word):
        currNode = self.wordTrie
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]
        currNode.end = True
        currNode.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        foundWords = []

        def search(node, r, c):
            if 0 > r or 0 > c or r >= len(board) or c >= len(board[0]):
                return

            if board[r][c] == '#':
                return

            char = board[r][c]

            if char not in node.children:
                return

            if node.children[char].end and not node.children[char].found:
                foundWords.append(node.children[char].word)
                node.children[char].found = True
            
            board[r][c] = '#'

            search(node.children[char], r + 1, c)
            search(node.children[char], r - 1, c)
            search(node.children[char], r, c + 1)
            search(node.children[char], r, c - 1)

            board[r][c] = char

        for r in range(len(board)):
            for c in range(len(board[0])):
                search(trie.wordTrie, r, c)

        return foundWords

