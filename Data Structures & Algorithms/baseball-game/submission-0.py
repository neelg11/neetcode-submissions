class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        nums=operations
        for i in range(0,len(nums)):
            if(nums[i]=='C'):
                ans.pop()
            elif(nums[i]=="+"):
                ans.append(int(ans[-1])+int(ans[-2]))
            elif(nums[i]=='D'):
                ans.append(int(ans[-1]*2))
            else:
                print(nums[i])
                ans.append(int(nums[i]))
        res=0
        while(len(ans)):
                res+=ans.pop()
        return res