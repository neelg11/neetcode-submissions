class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while(l<r):
            m=l+(r-l)//2
            if(nums[m]<nums[r]):
                r=m
                # r=m and not m-1 because nums[m] is possible candidate, less than nums[r]
            else:
                l=m+1
                # l=m+1 and not m because nums[m] is already bigger than nums[r] so rejected
            
        return nums[l]