class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=stones
        for i in range(len(maxheap)):
            maxheap[i]*=-1
        heapq.heapify(maxheap)
        while(len(maxheap)>1):
            a=-(heapq.heappop(maxheap))
            b=-(heapq.heappop(maxheap))
            if(a-b==0):
                continue
            heapq.heappush(maxheap,(-abs(a-b)))

        if(maxheap):
            return -maxheap[0]
        return 0
        
