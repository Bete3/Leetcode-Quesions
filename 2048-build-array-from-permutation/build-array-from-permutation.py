class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arry = []
        for i in range(len(nums)):
            arry.append(nums[nums[i]])
        return arry
