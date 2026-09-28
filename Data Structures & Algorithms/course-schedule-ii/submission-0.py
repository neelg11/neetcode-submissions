class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u,v in prerequisites:
                adj_list[v].append(u)
                indegree[u]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        path=[]
        while(q):
            node=q.popleft()
            path.append(node)
            for nei in adj_list[node]:
                indegree[nei]-=1
                if(indegree[nei]==0):
                    q.append(nei)            
        if len(path)==numCourses:
            return path
        return []