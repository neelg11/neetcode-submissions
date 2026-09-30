class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for x in times:
            adj[x[0]].append((x[1],x[2]))
        print(adj)
        dist=[100000]*(n+1)
        dist[k]=0
        heap=[(0,k)]
        while(heap):
            heap_dist_until_node, node = heapq.heappop(heap)
            if heap_dist_until_node > dist[node]:
                continue
            
            for nei, NEI_dist_from_node in adj[node]:
                NEW_dist_to_nei = NEI_dist_from_node + heap_dist_until_node
                
                if (NEW_dist_to_nei < dist[nei]):
                    dist[nei] = NEW_dist_to_nei
                    heapq.heappush(heap,(NEW_dist_to_nei, nei ))
        print(dist)
        ans=-100000
        for cost in dist[1:]:
            ans=max(cost,ans)
            if(ans==100000):
                return -1

        return ans