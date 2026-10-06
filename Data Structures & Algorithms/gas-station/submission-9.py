#two pointers
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end = n-1, 0
        for i in range(n):
            gas[i] = gas[i]-cost[i]

        tank = gas[start]
        while(end<start):
            if(tank>0):
                tank += gas[end]
                end += 1
            else:
                start -= 1
                tank += gas[start]
                
        return start if tank>=0 else -1
