class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            c = word[i]
            if c == '.':
                return any(k != '#' and dfs(i + 1, node[k]) for k in node)
            if c in node:
                return dfs(i + 1, node[c])
            return False
        return dfs(0, self.trie)









# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)