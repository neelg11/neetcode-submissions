class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        while(n!=0):
            for i in range(n-1):
                if(nums[i]>nums[i+1]): nums[i],nums[i+1]=nums[i+1],nums[i]
            n-=1
        return nums
