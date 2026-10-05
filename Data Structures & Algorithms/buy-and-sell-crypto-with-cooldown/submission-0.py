#top donw
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n+2)]
        def dfs(i, holding):
            if(i >= len(prices)):
                return 0
            if dp[i][holding]!=-1:
                return dp[i][holding]

            if(holding==0):
                dp[i][0] = max( dfs(i+1, 0), dfs(i+1, 1)-prices[i] )
                return dp[i][0]
            else:
                dp[i][1] = max(dfs(i+1, 1), dfs(i+2, 0) + prices[i])
                return dp[i][1]
        return dfs(0, 0)