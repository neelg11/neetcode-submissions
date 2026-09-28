#BFS KAHNS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u,v in prerequisites:
                adj_list[v].append(u)
                indegree[u]+=1
                
        order=[]
        def dfs(node):
            order.append(node)
            indegree[node]-=1000 # JUST TO AVOID Dfs call from the outer for loop again.
            for nei in adj_list[node]:
                indegree[nei]-=1
                if(indegree[nei]==0):
                    dfs(nei)

        for i in range(numCourses):
            if(indegree[i]==0):
                dfs(i)
        print(order)
        if len(order)==numCourses:
            return order
        return []