class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(cap):
            total = 0
            need_day = 1
            for w in weights:
                if total + w > cap:
                    need_day += 1
                    total = 0
                total += w
            return need_day <= days

        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right)//2
            if canship(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        