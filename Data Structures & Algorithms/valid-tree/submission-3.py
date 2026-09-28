class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited=set()

        def dfs(node, parent):
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei, node)
                elif(parent!=nei):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n