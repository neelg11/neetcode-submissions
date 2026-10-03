#Prefix & Suffix

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, suffix = 1, 1
        res = nums[0]
        for i in range(n):
            prefix = prefix * nums[i]
            res = max(res,prefix)
            if(prefix == 0):
                prefix = 1
        
        for i in range(n-1, -1, -1):
            suffix = suffix * nums[i]
            res = max(res, suffix)
            if(suffix == 0):
                suffix = 1
        return res