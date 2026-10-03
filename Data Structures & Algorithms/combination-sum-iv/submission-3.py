# more than 2 option per step, for loop
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)
        def dfs(target):
            if (target==0): return 1
            if (target<0):  return 0
            if dp[target] != -1:
                return dp[target]
           
            res = 0
            for num in nums:
                if(target-num>=0):
                    res += dfs(target-num)
            dp[target] = res
            return dp[target]
        return dfs(target)