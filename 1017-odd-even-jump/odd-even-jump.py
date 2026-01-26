class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True

        idx = sorted(range(n), key=lambda i: (arr[i], i))
        stack = []
        next_higher = [None] * n
        for i in idx:
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        idx = sorted(range(n), key=lambda i: (-arr[i], i))
        stack = []
        next_lower = [None] * n
        for i in idx:
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        for i in range(n - 2, -1, -1):
            if next_higher[i] is not None:
                odd[i] = even[next_higher[i]]
            if next_lower[i] is not None:
                even[i] = odd[next_lower[i]]

        return sum(odd)