class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arry = []
        for i in range(len(words)):
            for j in range(len(words[i])):
                if x in words[i]:
                    arry.append(i)
                    break
        return(arry)