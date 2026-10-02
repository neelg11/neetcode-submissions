class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1
        for num in nums:
            new_currMin = min(num*curr_max, num * curr_min, num)
            new_currMax = max(num*curr_max, num * curr_min, num)
            
            curr_min = new_currMin
            curr_max = new_currMax
            res = max(res, curr_max)
        
        return res
