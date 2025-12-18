class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        r = word.index(ch)
        l = 0
        lst = list(word)
        while l < r:
            lst[l],lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return "".join(lst)


        


        