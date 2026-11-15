class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        
        visited = [False] * n
        def dfs(i):
            for nei in adj_list[i]:
                if visited[nei]:
                    continue
                visited[nei] = True
                dfs(nei)
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans
                
                
            

        
