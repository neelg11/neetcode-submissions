class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in nums:
            sum+=i
        return ((n*(n+1))//2) - sum