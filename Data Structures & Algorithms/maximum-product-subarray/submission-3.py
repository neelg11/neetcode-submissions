#Prefix & Suffix shorter code

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, suffix = 0, 0
        res = nums[0]
        for i in range(n):
            prefix = nums[i] * (prefix or 1) #if prefix 0 then 1
            suffix = nums[n-i-1] * (suffix or 1) #if suffix 0 then 1
            res = max(res, prefix, suffix)
        return res