class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1,-1,-1):
            points, brainpower = questions[i] 
            next_question = i + brainpower + 1
            solve = points
            if next_question <= n:
                solve = solve + dp[next_question]
            skip = dp[i+1]
            dp[i] = max(solve,skip)
        return dp[0]