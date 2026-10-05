class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = 0
        for i in range(n):
            if(i>reachable):
                return False
            new = i+nums[i]
            if(new>reachable):
                reachable = new
        return True