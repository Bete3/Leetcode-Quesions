class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = 0
        for i in range(n):
            remain = n - i
            if prefix + arr[i] * remain >= target:
                v = (target - prefix) / remain
                a = int(v)
                b = a + 1
                sa = prefix + a * remain
                sb = prefix + b * remain
                if abs(sa - target) <= abs(sb - target):
                    return a
                return b
            prefix += arr[i]
        return arr[-1]