class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        xor=0
        n=len(nums)
        def dfs(i):
            nonlocal ans,xor
            # nonlocal xor
            if(i>=n):
                ans+=xor
                return
            
            dfs(i+1)
            xor^=nums[i]
            dfs(i+1)
            xor^=nums[i]
        dfs(0)
        return ans