class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans=[]
        path=[]
        sum=0
        n=len(nums)
        def dfs(i):
            nonlocal ans,path,sum
            if(sum==target):
                ans.append(path.copy())
                return
            if(sum>target):
                    return
            for j in range(i,n):
                # if(sum+nums[j]>target):
                #     return
                sum+=nums[j]
                path.append(nums[j])
                dfs(j)
                path.pop()
                sum-=nums[j]
        dfs(0)
        return ans