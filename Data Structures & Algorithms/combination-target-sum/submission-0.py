class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path=[]
        ans=[]
        sum=0
        n=len(nums)
        def dfs(i):
            nonlocal sum
            if(sum==target):
                ans.append(path.copy())
                return
            if(i>=n or sum>target):
                return
            dfs(i+1)
            path.append(nums[i])
            sum+=nums[i]
            dfs(i)
            path.pop()
            sum-=nums[i]
        dfs(0)
        return ans