class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        end = 0
        for _, r in intervals:
            if r > end:
                res += 1
                end = r
        return res