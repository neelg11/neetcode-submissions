class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a,b=0,0
        count_a,count_b=0,0
        for i in range(len(nums)):
            if(nums[i]==a):
                count_a+=1
            elif(nums[i]==b):
                count_b+=1
            elif count_a==0:
                a=nums[i]
                count_a=1
            elif count_b==0 and nums[i]!=a:
                b=nums[i]
                count_b=1
            else:
                count_a-=1
                count_b-=1
                
        count_a,count_b=0,0
        for i in nums:
            if(i==a):
                count_a+=1
            elif(i==b):
                count_b+=1
        ans=[]
        
        if(count_a>(n//3)): ans.append(a)
        if(count_b>n//3): ans.append(b)
        return ans
            
                
