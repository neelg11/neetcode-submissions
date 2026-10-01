class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        dist = [float('inf')]*n
        edges, mst = 0, 0
        curr_node = 0
        visit = [False]*n
        while(edges < n-1):

            visit[curr_node] = True
            next_node = -1
            x, y = points[curr_node][0], points[curr_node][1]
            for i in range(n):
                if(visit[i]):
                    continue
                
                a, b = points[i][0], points[i][1]

                man_dist = abs(x-a) + abs(y-b)

                if(man_dist < dist[i]):
                    dist[i] = man_dist

                if(next_node == -1 or dist[i]<dist[next_node]):
                    next_node = i
            
            mst += dist[next_node]
            edges+=1
            curr_node = next_node
        return mst