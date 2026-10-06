class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        dp = [[False]* (n+2) for _ in range(n+2)]
        dp[len(s)][1] = True
        for i in range(n-1,-1,-1):
            for j in range(1, len(s)+1):
                if(s[i]=='('):
                    dp[i][j] = dp[i+1][j+1]
                if(s[i]==')'):
                    dp[i][j] = dp[i+1][j-1]
                if(s[i]=='*'):
                    dp[i][j] = dp[i+1][j-1] or dp[i+1][j] or dp[i+1][j+1]
        print(dp)
        return dp[0][1]
