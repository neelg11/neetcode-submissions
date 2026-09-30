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
            dis, node = heapq.heappop(heap)
            if(dis>dist[node]):
                continue

            for nei, nei_dis in adj[node]:
                new_dis=max(dis,nei_dis)
                
                if(new_dis<dist[nei]):
                    dist[nei]=new_dis
                    heapq.heappush(heap,(new_dis,nei))
        
        return dist[(n*m)-1]