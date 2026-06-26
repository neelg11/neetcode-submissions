class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        i=0
        while(i<l-1):
            j=0
            while(j<l-1-i):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                j=j+1
            if nums[i]<=nums[i+1]:
                i=i+1
        return nums