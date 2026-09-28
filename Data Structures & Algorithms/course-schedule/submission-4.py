class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_list[v].append(u)
        
        visited=set()
        path=set()
        def dfs(node):
            visited.add(node)
            path.add(node)
            for nei in adj_list[node]:
                if(nei in path):
                    return False
                elif nei not in visited:
                    if not dfs(nei):
                        return False
            path.remove(node)
            return True
                
        for u,v in prerequisites:
            if v not in visited:
                if not dfs(v):
                    return False
        return True