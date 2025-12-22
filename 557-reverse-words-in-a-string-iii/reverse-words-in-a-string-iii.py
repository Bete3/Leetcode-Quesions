class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        rever = [word[::-1] for word in words]
        return ' '.join(rever)
        