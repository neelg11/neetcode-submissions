class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0
        n=len(nums)
        ans=1000000
        curr_sum=0
        for r in range(n):
            if curr_sum<target:
                curr_sum+=nums[r]
            while curr_sum>=target:
                ans=min(ans, r-l+1)
                curr_sum-=nums[l]
                l+=1
        return ans%1000000
