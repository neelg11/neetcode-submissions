class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)
        return nums[l//2]

