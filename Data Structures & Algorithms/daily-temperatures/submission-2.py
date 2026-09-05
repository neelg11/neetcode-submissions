class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i,num in enumerate(temperatures):
            if(len(stack)==0 or temperatures[stack[-1]]>=num):
                stack.append(i)
            else:
                while(stack and temperatures[stack[-1]]<num):
                    popped=stack.pop()
                    ans[popped]=i-popped
                stack.append(i)
        return ans
                
