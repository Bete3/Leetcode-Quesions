class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        END = "#"

        for root in dictionary:
            node = trie
            for c in root:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[END] = root

        def replace(word):
            node = trie
            for c in word:
                if c not in node:
                    return word
                node = node[c]
                if END in node:
                    return node[END]
            return word

        return " ".join(replace(w) for w in sentence.split())