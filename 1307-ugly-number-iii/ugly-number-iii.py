class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x,y):
            return x * y // math.gcd(x,y)
        ab = lcm(a,b)
        ac = lcm(a,c)
        bc = lcm(b,c)
        abc = lcm(ab,c)
        def cnt(x):
            return (x//a) + (x//b) + (x//c) \
             - (x//ab) - (x//ac) - (x//bc) \
             + (x//abc)

        left = 1
        right = 2 * 10**9
        while left < right:
            mid = (left + right)//2

            if cnt(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left