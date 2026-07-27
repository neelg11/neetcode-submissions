class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            c=l+(r-l)//2
            print(f"l:{l},r:{r},c:{c}")
            if(nums[c]==target): return c
            if(l==r):
                if(nums[l]<target): return l+1
                else: return l
            elif(nums[c]>target):r=c
            else: l=c+1
        return l+1