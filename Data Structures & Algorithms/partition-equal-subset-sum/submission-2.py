#Bottom Up
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if(target%2==1):
            return False
        target = target // 2
        dp = [[False]*(n+1) for _ in range(target+1)]
        dp[0] = [True] * (n+1)
        for j in range(n-1, -1, -1):
            for i in range(target, -1, -1):
                dp[i][j] = dp[i][j+1]
                if not dp[i][j]:
                    if(i>=nums[j] and dp[i-nums[j]][j+1]):
                        dp[i][j] = True
        return dp[target][0]