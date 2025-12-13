class Solution:
    def maxDistinct(self, s: str) -> int:
        val = set()
        for i in range(len(s)):
            val.add(s[i])
        return len(val)
        