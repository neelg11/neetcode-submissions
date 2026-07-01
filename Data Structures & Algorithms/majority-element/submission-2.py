class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)
        n=l//2
        count=1
        for i in range(1,l):
            if(nums[i]==nums[i-1]):
                count+=1
                if count>n:
                    return nums[i]
            else:
                count=1
        return nums[l-1]

