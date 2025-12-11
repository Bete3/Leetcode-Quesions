class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cunt = 0
        for num in nums:
            if num % 3 != 0:
                if (num -1) % 3 == 0:
                    cunt += 1
                elif (num + 1) % 3 == 0:
                    cunt += 1
        return cunt

        