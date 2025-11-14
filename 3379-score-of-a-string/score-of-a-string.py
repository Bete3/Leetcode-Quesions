class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        diff = 0
        for i in range (len(s) - 1):
            diff = ord(s[i]) - ord(s[i + 1])
            #print(ord(s[i]))
            total += abs(diff)
        return total
        