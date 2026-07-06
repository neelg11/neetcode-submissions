class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        i=0
        if(len(nums)<2): return 0
        while(True):
            mx=0
            argmax=-1
            for j in range(1,nums[i]+1):
                if(i+nums[i]>=len(nums)-1): return count+1

                mx=max(mx,(i+j)+nums[i+j])
                if((i+j)+nums[i+j] == mx):
                    argmax=i+j
            i=argmax
            count+=1
            
        return count