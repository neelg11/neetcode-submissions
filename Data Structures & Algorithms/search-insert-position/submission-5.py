class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        c=0
        while(i<=j):
            c=(i+j)//2
            if(nums[c]==target):
                return c
            elif(nums[c]<target):
                i=c+1
            else:
                j=c-1
        return i