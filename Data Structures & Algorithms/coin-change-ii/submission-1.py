class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1]*len(coins) for _ in range(amount+1)]
        def dfs(target, x):
            if(target == 0):
                return 1
            if(dp[target][x]!=-1):
                return dp[target][x]
            res = 0
            for i in range(x, len(coins)):
                if(target>=coins[i]):
                    res+=dfs(target-coins[i], i)
            dp[target][x] = res
            return res
        return dfs(amount, 0)