import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        res = [-1] * len(queries)
        heap = []
        i = 0
        n = len(intervals)
        for idx in order:
            q = queries[idx]
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[idx] = heap[0][0]
        return res
                        
        