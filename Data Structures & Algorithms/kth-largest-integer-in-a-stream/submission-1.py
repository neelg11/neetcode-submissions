import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=nums
        hq.heapify(self.heap)

    def add(self, val: int) -> int:
        hq.heappush(self.heap,val)
        return hq.nlargest(self.k,self.heap)[-1]
