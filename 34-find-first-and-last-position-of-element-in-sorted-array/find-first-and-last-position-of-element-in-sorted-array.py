class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first =0
        last = 0
        if target not in nums:
            return [-1,-1]
        if target in nums:
            for i in range(0,len(nums)):
                if(nums[i]==target):
                    first = i
                    break
            for j in range(len(nums)-1,-1,-1):
                if(nums[j] == target):
                    last = j
                    break
            return [first,last]