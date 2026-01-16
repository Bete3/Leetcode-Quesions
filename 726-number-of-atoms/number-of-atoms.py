class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j] or 1)
                top = stack.pop()
                for elem in top:
                    stack[-1][elem] += top[elem] * multiplier
                i = j
            else:
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                elem = formula[i:j]
                i = j
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j] or 1)
                stack[-1][elem] += count
                i = j

        res = ""
        for elem in sorted(stack[-1]):
            cnt = stack[-1][elem]
            res += elem + (str(cnt) if cnt > 1 else "")
        return res