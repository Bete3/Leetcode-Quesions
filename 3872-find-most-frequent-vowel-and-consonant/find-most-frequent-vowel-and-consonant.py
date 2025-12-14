class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = "aeiou"
        c = {}
        vo = {}
        for ch in s:
            if ch in v:
                if ch in vo:
                    vo[ch] += 1
                else:
                    vo[ch] = 1
            else:
                if ch in c:
                    c[ch] += 1
                else:
                    c[ch] = 1
        mc = 0
        mv = 0
        for ch in c:
            if mc < c[ch]:
                mc = c[ch]
        for ch in vo:
            if mv < vo[ch]:
                mv = vo[ch]
        total = mc + mv
        return total




                

        