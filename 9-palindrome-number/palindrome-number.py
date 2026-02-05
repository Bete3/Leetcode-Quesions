class Solution:
    def isPalindrome(self, x: int) -> bool:
        str(x)
        rev = str(x)[::-1]
        return str(x) == rev
        
        