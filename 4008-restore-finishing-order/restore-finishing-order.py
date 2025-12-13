class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arry = []
        for i in range(len(order)):
            if order[i] in friends:
                arry.append(order[i])
        return arry
        