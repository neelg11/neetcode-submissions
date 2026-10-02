class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(target, i):
            if(i >= len(nums)):
                return False
            if(nums[i]==target):
                return True
            return dfs(target-nums[i], i+1) or dfs(target, i+1)
        target = sum(nums)
        if(target%2==0):
            return dfs(target//2, 0)
        return False