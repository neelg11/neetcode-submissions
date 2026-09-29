class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        parent=[i for i in range(n)]
        size = [1]*n

        def find(x):
            p=parent[x]
            while(p != parent[p]):
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(u,v):
            ru, rv = find(u), find(v)
            if(ru==rv):
                return False
            else:
                parent[rv]=ru
                size[ru]+=size[rv]
            return True
        ans=[]
        for u,v in edges:
            if not union(u,v):
                ans=[u,v]
        return ans
            


