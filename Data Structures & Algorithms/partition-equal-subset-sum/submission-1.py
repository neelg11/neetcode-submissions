class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if(target%2):
            return False
        target = target // 2

        dp = [[-1]*(target+1) for _ in range(n)]
        def dfs(i, target):
            if(i>=n):
                return target == 0
            if(target<0):
                return False
            if(dp[i][target]!=-1):
                return dp[i][target]
            dp[i][target] =  dfs(i+1, target-nums[i]) or dfs(i+1, target)
            return dp[i][target]
        return dfs(0, target)