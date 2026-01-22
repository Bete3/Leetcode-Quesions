class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        full = (1 << m) - 1
        dp = [float('inf')] * (1 << m)
        dp[0] = 0

        sc = []
        for s in stickers:
            cnt = {}
            for c in s:
                cnt[c] = cnt.get(c, 0) + 1
            sc.append(cnt)

        for mask in range(1 << m):
            if dp[mask] == float('inf'):
                continue
            for s in sc:
                newmask = mask
                cnt = dict(s)
                for i in range(m):
                    if not (newmask >> i) & 1 and cnt.get(target[i], 0) > 0:
                        newmask |= 1 << i
                        cnt[target[i]] -= 1
                dp[newmask] = min(dp[newmask], dp[mask] + 1)

        return -1 if dp[full] == float('inf') else dp[full]






