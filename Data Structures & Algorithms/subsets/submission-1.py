#recurssion
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def dfs(curr_set,i):
            if(i>=n):
                ans.append(curr_set)
                return
            dfs(curr_set,i+1)
            temp=curr_set.copy()
            temp.append(nums[i])
            dfs(temp,i+1)
        dfs([],0)
        return ans