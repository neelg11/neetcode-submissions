class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        count=nums.count(val)
        while(i<j):
            while(j>=0 and nums[j]==val): 
                j-=1
            while(i<len(nums) and nums[i]!=val):i+=1
            if(i<j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1        
        return (len(nums)-count)