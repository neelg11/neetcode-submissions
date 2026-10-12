class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        while(r<len(nums)):
            if(nums[r] != val):
                nums[l] = nums[r]
                l+=1
            else:
                nums[l] = nums[r]
            r+=1
        return l