class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        while(n!=0):
            for i in range(n-1):
                if(nums[i]>nums[i+1]): nums[i],nums[i+1]=nums[i+1],nums[i]
            n-=1
        return nums
