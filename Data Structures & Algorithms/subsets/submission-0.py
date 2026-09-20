class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        def subset(currset,i,nums):
            if(i>=len(nums)): return
            #not pick
            subset(currset,i+1,nums)
            #pick
            temp=currset.copy()
            temp.append(nums[i])
            ans.append(temp)
            subset(temp,i+1,nums)

        subset([],0,nums)
        return ans
