class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_list[v].append(u)
        
        visited=set()
        path=set()
        order=[]
        def dfs(node):
            visited.add(node)
            path.add(node)
            for nei in adj_list[node]:
                if nei in visited:
                    if(nei in path):
                        return False
                else:
                    if not dfs(nei):
                        return False
            path.remove(node)
            order.append(node)
            return True
                
        for v in range(numCourses):
            if v not in visited:
                if not dfs(v):
                    return []
        order.reverse()
        return order