class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if(r == len(nums)-1 or nums[r] != nums[r+1]):
                nums[l] = nums[r]
                l+=1

        return l