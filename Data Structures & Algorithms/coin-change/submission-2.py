#top down dp, at each step the choices are len(coins)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        def dfs(target):
            if(target==0):
                return 0
            if(dp[target] != -1):
                return dp[target]
            res = 1e9
            for coin in coins:
                if(target - coin >= 0):
                    res = min(res, 1+dfs(target-coin))
            dp[target] = res
            return dp[target]

        ans = dfs(amount)
        return -1 if ans==1e9 else ans