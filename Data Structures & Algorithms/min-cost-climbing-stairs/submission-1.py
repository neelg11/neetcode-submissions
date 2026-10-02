class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        if(len(cost)==2):
            return min(first, second)
        i = 2
        while(i<len(cost)):
            temp = second
            second = min(first, second) + cost[i]
            first = temp
            i+=1
        return min(first, second)
    