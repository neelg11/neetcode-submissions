"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        n = len(intervals)
        if(n<2): return True
        l, r = intervals[0].start, intervals[0].end
        n = len(intervals)
        for i in range(1,n):
            u, v = intervals[i].start, intervals[i].end
            print(f"l:{l} ,r:{r} ,u:{u} ,v:{v}")
            if(l<=u<r or l<v<=r):
                return False
            l = min(l,u)
            r = max(r,v)
        return True

            