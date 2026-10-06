class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas[i]-=cost[i]
        start = -1
        curr_gas = 0

        for i in range(2*n):
            if i%n == start:
                break
            curr_gas += gas[i%n]
            if(curr_gas<0):
                start = -1
                curr_gas = 0
            elif(i<n and start==-1):
                start = i%n
        
        return start
        