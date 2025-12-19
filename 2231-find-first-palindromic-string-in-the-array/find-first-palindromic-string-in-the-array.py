class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        '''for i in range(len(words):
            l = 0
            r = len(words) - 1
            while l < r:
                if word[i][l] != word[i][r]:
                    break
                else:
                    l += 1
                    r -= 1'''
        for i in range(len(words)):

            if words[i] != words[i][::-1]:
                continue
            else:
                return words[i]
    
        return ""
        
            
    

        