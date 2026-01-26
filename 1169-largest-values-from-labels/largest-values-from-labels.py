class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used = {}
        res = 0
        taken = 0
        for v, l in items:
            if taken == numWanted:
                break
            if used.get(l, 0) < useLimit:
                res += v
                used[l] = used.get(l, 0) + 1
                taken += 1
        return res






