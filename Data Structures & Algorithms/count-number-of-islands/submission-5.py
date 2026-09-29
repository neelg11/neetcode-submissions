##DSU

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        parent = [i for i in range(n*m)]
        size = [1 for _ in range(n*m)]

        def find(x):
            if(parent[x]==x):
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            root_a, root_b = find(a), find(b)
            
            if(root_a==root_b):
                return
            if(size[root_a]<size[root_b]):
                root_a, root_b = root_b,root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
        
        count=0
        for r in range(n):
            for c in range(m):
                if(grid[r][c]=='1'):
                    count+=1


        for r in range(n):
            for c in range(m):

                curr_id = r * m + c
                if(grid[r][c]=='0'):
                    continue
                
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    
                    if(0 <= nr < n and 0 <= nc < m and grid[nr][nc]=='1'):
                        nei_id = nr * m + nc
                        if(find(curr_id)!=find(nei_id)):
                            union(curr_id, nei_id)
                            count-=1
        # return count
        ans=0
        for r in range(n):
            for c in range(m):
                if(grid[r][c]=='1'):
                    id = r * m + c
                    if(find(id)==id):
                        ans+=1

        return ans





