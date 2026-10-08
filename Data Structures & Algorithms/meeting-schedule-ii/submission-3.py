"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        minheap = []
        ans = 0
        for interval in intervals:
            while minheap and minheap[0] <= interval.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, interval.end)
            ans = max(len(minheap), ans)
        return ans

