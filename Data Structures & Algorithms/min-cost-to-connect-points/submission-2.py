class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if(n<2):
            return 0
        edges=[]
        
        for i in range(n):
            for j in range(i,n):
                if i==j:
                    continue
                x,y=points[i]
                a,b=points[j]
                cost = abs(x-a) + abs(y-b)
                edges.append([cost,i,j])

        edges.sort()
        parent = [i for i in range(n)]
        size    = [1 for _ in range(n)]

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
        mst, count = 0, 0
        for cost, u, v in edges:
            if union(u,v):
                mst+=cost
                count+=1
            else: 
                continue
            if count==n-1:
                return mst

            

