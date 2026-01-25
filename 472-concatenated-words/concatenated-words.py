class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        res = []

        def can_form(word):
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[-1]

        for w in words:
            word_set.remove(w)
            if can_form(w):
                res.append(w)
            word_set.add(w)

        return res