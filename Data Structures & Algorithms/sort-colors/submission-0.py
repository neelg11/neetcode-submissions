class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        i=0
        while(i<l-1):
            j=i+1
            while(j<l):
                if(nums[i]>nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
                j+=1
            i+=1