class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        flag=1
        j=len(nums)-1
        while(i<=j):
            c=(i+j)//2
            if(nums[c]==target):
                return c
            elif(nums[c]<target):
                i=c+1
            else:
                j=c-1
        return -1
        