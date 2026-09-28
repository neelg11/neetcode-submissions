class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=[[] for _ in range(n)]
        for edge in edges:
            u,v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False]*n
        def bfs(root):
            q=deque()
            q.append(root)
            while(q):
                node=q.popleft()
                visited[node]=True
                for neighbour in adj_list[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        q.append(neighbour)

        ans=0
        for node in range(n):
            if(not visited[node]):
                bfs(node)
                ans+=1
        return ans