class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def dfs(i, expr, val, last):
            if i == len(num):
                if val == target:
                    res.append(expr)
                return
            for j in range(i + 1, len(num) + 1):
                if j > i + 1 and num[i] == '0':
                    break
                cur = int(num[i:j])
                if i == 0:
                    dfs(j, str(cur), cur, cur)
                else:
                    dfs(j, expr + '+' + str(cur), val + cur, cur)
                    dfs(j, expr + '-' + str(cur), val - cur, -cur)
                    dfs(j, expr + '*' + str(cur), val - last + last * cur, last * cur)
        
        dfs(0, "", 0, 0)
        return res