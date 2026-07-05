class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=0
        l=len(nums)
        if(l==1):
            return l
        while(i<l):
            if(nums[i]==nums[i-1]):
                nums.remove(nums[i])
                l-=1
            else:
                i+=1
        return l