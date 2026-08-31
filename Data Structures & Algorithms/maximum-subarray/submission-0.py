class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        res=-110000000
        for i,num in enumerate(nums):
            curr_sum+=num
            res=max(curr_sum,res)
            if(curr_sum<=0):
                curr_sum=0
        return res