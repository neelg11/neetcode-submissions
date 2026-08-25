class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        zeros,twos=0,n-1
        i=0
        while(i<n):
            if(nums[i]==1 or (i==n-1 and nums[i]==2)):
                i+=1
            elif(nums[i]==0):
                if(i>zeros):
                    nums[zeros],nums[i]=nums[i],nums[zeros]
                    zeros+=1
                else:
                    i+=1
            elif(nums[i]==2):
                if(i<twos):
                    nums[twos],nums[i]=nums[i],nums[twos]
                    twos-=1
                else:
                    i+=1
            