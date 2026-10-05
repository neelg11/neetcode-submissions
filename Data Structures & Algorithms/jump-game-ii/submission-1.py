class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1000]*n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i, i+nums[i]+1):
                if(j>=len(nums)):
                    break
                dp[i] = min(dp[i], dp[j]+1)
        print(dp)
        return dp[0]