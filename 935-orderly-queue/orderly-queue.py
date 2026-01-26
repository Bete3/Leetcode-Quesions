class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        best = s
        for i in range(1, len(s)):
            t = s[i:] + s[:i]
            if t < best:
                best = t
        return best






