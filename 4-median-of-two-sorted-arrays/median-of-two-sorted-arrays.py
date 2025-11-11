class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A,B = B,A
        left = 0
        right = len(A) - 1
        while True:
            i = (left + right)//2
            j = half - i - 2
            if i >= 0:
                Aleft = A[i]
            else:
                Aleft = float("-inf")
            if (i + 1) < len(A):
                Aright = A[i + 1]
            else:
                Aright = float("inf")
            if j >= 0:
                Bleft = B[j]
            else:
                Bleft = float("-inf")

            if (j + 1) < len(B):
                Bright = B[j + 1]
            else:
                Bright = float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    median = min(Aright, Bright)
                    return median
                else:
                    median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                    return median
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1