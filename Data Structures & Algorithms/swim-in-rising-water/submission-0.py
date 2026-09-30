class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dist=[float('inf')]*(n*n)
        dist[0]=(grid[0][0])
        heap=[(dist[0],0)]
        adj=[[] for _ in range(n*n)]
        directions=[(0,1), (1,0)]
        for i in range(n):
            for j in range(n):
                id= i*n + j
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc
                    if(nr>=n or nc>=n):
                        continue
                    new_id= nr*n + nc
                    adj[id].append((new_id, max(grid[i][j], grid[nr][nc])))
                    adj[new_id].append((id, max(grid[i][j], grid[nr][nc])))

        while(heap):
            heap_dist_until_node, node = heapq.heappop(heap)
            if heap_dist_until_node > dist[node]:
                continue
            
            for nei, NEI_dist_from_node in adj[node]:
                NEW_dist_to_nei = max(NEI_dist_from_node, heap_dist_until_node)
                
                if (NEW_dist_to_nei < dist[nei]):
                    dist[nei] = NEW_dist_to_nei
                    heapq.heappush(heap,(NEW_dist_to_nei, nei ))
        
        return dist[(n*n)-1]