class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #Kartik's: search pivot, then binary search on left array and right array
        n=len(nums)
        l,r=0,n-1
        while(l<r):
            m=l+(r-l)//2
            if(nums[m]<nums[r]):
                r=m
                # r=m and not m-1 because nums[m] is possible candidate, less than nums[r]
            else:
                l=m+1
                # l=m+1 and not m because nums[m] is already bigger than nums[r] so rejected
        pivot=l
        l,r=0,n-1
        if(nums[pivot]<=target<=nums[r]):
            l=pivot
        else:
            r=pivot
        while(l<=r):
            m=l+(r-l)//2
            if(nums[m]==target): return m
            elif(nums[m]<target): l=m+1
            else: r=m-1
        return -1
        