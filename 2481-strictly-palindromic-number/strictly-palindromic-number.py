class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(n,b):
            s = ""
            while n > 0:
                s += str(n % b)
                n //= b
            return s
        for b in range(2, n-1):
            s = convert(n,b)
            if s != s[::-1]:
                return False
        return True
