#Kruskals: just keep adding minimum edge until the 2 nodes are connect

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        edges=[]
        n=len(heights)
        m=len(heights[0])
        if(n*m<=1):
            return 0
        for i in range(n):
            for j in range(m):
                for dr, dc in ((0,1), (1,0)):
                    nr = i+dr
                    nc = j+dc
                    if(nr<n and nc<m):
                        cost = abs(heights[nr][nc]-heights[i][j])
                        edges.append((cost, i*m + j, nr*m + nc))
        edges.sort()
        parent = [i for i in range(n*m)]
        size    = [1 for _ in range(n*m)]
        def find(x):
            if(parent[x]==x):
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            root_a, root_b = find(a), find(b)
            if(root_a == root_b):
                return False
            if(size[root_a]<size[root_b]):
                root_a, root_b = root_b, root_a
            parent[root_b]=root_a
            size[root_a]+=size[root_b]
            return True

        for cost, u, v in edges:
            if union(u,v):
                if(find(0)==find((m*n)-1)):
                    return cost
