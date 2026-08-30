class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a,count_a=0,0
        for i in range(len(nums)):
            if(count_a==0):
                count_a=1
                a=nums[i]
            elif(nums[i]==a):
                count_a+=1
            else:
                count_a-=1
        return a