class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        parent=[i for i in range(n)]
        size = [1]*n

        def find(x):
            if parent[x]==x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]

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
            


