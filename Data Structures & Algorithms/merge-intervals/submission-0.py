class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        curr = intervals[0]
        ans = []
        n=len(intervals)
        for i in range(1, n):
            if(intervals[i][0]<=curr[1]):
                curr = [min(intervals[i][0], curr[0]), max(intervals[i][1], curr[1])]
            else:
                ans.append(curr)
                curr = intervals[i]
        ans.append(curr)
        return ans
