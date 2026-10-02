class Solution:
    def integerBreak(self, n: int) -> int:
        if n<4: return n-1
        if n==4: return n
        dp = [0] * (n+1)
        dp[2], dp[3], dp[4] = 2, 3, 4
        for i in range(5, n+1):
            for j in range(2,i):
                dp[i] = max( dp[i], dp[i-j]*dp[j] )
        return dp[n]