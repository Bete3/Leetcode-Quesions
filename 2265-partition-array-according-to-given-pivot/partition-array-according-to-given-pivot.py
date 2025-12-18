class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        for i, j in zip(range(len(nums)), range(len(nums)-1,-1,-1)):
            if nums[i] < pivot:
                result[l] = nums[i]
                l += 1
            if nums[j] > pivot:
                result[r] = nums[j]
                r -= 1
        while l <= r:
            result[l] = pivot
            l += 1
        return result 