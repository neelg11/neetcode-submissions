class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict((int))
        dp[0] = 1
        #dp[list_idx][dict_key]

        for i in range(n):
            new_dp  = defaultdict(int)
            for curr_sum, count in dp.items():
                new_dp[curr_sum+nums[i]]+=count
                new_dp[curr_sum-nums[i]]+=count
            dp = new_dp
        return dp[target]
            