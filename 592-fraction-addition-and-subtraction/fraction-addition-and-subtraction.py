class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        den = 1
        i = 0
        n = len(expression)

        while i < n:
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                if expression[i] == '-':
                    sign = -1
                i += 1

            a = 0
            while i < n and expression[i].isdigit():
                a = a * 10 + int(expression[i])
                i += 1
            a *= sign

            i += 1
            b = 0
            while i < n and expression[i].isdigit():
                b = b * 10 + int(expression[i])
                i += 1

            num = num * b + a * den
            den *= b
            g = math.gcd(abs(num), den)
            num //= g
            den //= g

        return f"{num}/{den}"