


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.visited = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word):
        curr = self.trie
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word, i):
        curr = self.trie
        res = []
        while i < len(word):
            ch = word[i]
            if ch not in curr.children:
                break
            curr = curr.children[ch]
            i += 1
            if curr.end:
                res.append(i)
        return res


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            arr = trie.search(s, i)
            for endI in arr:
                if dp[endI]:
                    dp[i] = True
                    break
        
        return dp[0]