class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i = 0
        for interval in intervals:
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            
            elif (newInterval[0] > interval[1]):
                ans.append(interval)
            
            else:
                newInterval[0] = min(interval[0],  newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            i+=1
        ans.append(newInterval)
        return ans

