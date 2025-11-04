class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []

        def dp(i, xor):
            nonlocal res
            if i == len(nums):
                res.append(xor)
                return 

            dp(i+1, xor ^ nums[i]) # take
            dp(i+1, xor) # skip

        dp(0, 0)
        return sum(res)

