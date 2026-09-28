class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=[[] for _ in range(n)]
        for edge in edges:
            u,v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False]*n
        def dfs(root):
            for neighbour in adj_list[root]:
                if(visited[neighbour]):
                    continue
                visited[neighbour]=True
                dfs(neighbour)
        ans=0
        for node in range(n):
            if not visited[node]:
                ans+=1
                dfs(node)
        return ans
