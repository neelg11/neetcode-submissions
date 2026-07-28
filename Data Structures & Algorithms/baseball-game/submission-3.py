class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        res=0
        nums=operations
        for i in range(0,len(nums)):
            if(nums[i]=='C'):
                res-=ans.pop()
            elif(nums[i]=="+"):
                res+=int(ans[-1])+int(ans[-2])
                ans.append(int(ans[-1])+int(ans[-2]))
                
            elif(nums[i]=='D'):
                res+=int(ans[-1]*2)
                ans.append(int(ans[-1]*2))
            else:
                ans.append(int(nums[i]))
                res+=int(nums[i])
        return res