class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = 0
        for i in range(n):
            if(i>reachable):
                return False
            reachable = max(reachable, i+nums[i])
        return True