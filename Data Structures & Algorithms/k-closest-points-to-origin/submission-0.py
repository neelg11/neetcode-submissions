class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return -1*math.sqrt(x**2+y**2)
        maxheap=[]
        for point in points:
            heapq.heappush(maxheap, (distance(point[0],point[1]) ,point) )
            if(len(maxheap)>k):
                heapq.heappop(maxheap)
        ans=[]
        for point in maxheap:
            ans.append(point[1])
        return ans
        

