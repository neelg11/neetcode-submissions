#Prims
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        visited=set()
        mst=0
        heap=[(0,0)]
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        while(heap):
            cost, node = heapq.heappop(heap)
            if (node in visited):
                continue
            mst+=cost
            visited.add(node)
            for nei_cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,(nei_cost,nei))

        return mst            
