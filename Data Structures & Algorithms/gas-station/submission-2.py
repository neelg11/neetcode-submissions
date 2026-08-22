
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        possible=0
        for i in range(len(gas)):
            gas[i]=gas[i]-cost[i]
            possible+=gas[i]
        if(possible<0): 
            return -1
            
        ans=-1
        curr_tank=0
        prev_tank=0
        n=len(gas)-1
        for i in range(n+1):
            curr_tank+=gas[n-i]
            if(curr_tank>=prev_tank):
                ans=n-i
                prev_tank=curr_tank
            
        return ans
#[2,-1,-1]



