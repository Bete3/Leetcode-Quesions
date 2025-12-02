class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        total = sum(nums)
        if total % k == 0:
            return count
        while total % k != 0:
            total -= 1
            count += 1
        return count
        