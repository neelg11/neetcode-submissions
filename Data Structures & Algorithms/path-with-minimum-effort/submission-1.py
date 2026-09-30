class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        dist=[float('inf')]*(n*m)
        dist[0]=0
        heap=[(0,0)]
        adj=[[] for _ in range(n*m)]
        directions=[(0,1), (1,0)]
        for i in range(n):
            for j in range(m):
                id= i*m + j
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc
                    if(nr>=n or nc>=m):
                        continue
                    new_id= nr*m + nc
                    adj[id].append((new_id, abs(heights[i][j]-heights[nr][nc])))
                    adj[new_id].append((id, abs(heights[i][j]-heights[nr][nc])))

        while(heap):
            heap_dist_until_node, node = heapq.heappop(heap)
            if heap_dist_until_node > dist[node]:
                continue
            
            for nei, NEI_dist_from_node in adj[node]:
                NEW_dist_to_nei = max(NEI_dist_from_node, heap_dist_until_node)
                
                if (NEW_dist_to_nei < dist[nei]):
                    dist[nei] = NEW_dist_to_nei
                    heapq.heappush(heap,(NEW_dist_to_nei, nei ))
        
        return dist[(n*m)-1]