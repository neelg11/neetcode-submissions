class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u,v in prerequisites:
                adj_list[v].append(u)
                indegree[u]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finished=0
        while(q):
            node=q.popleft()
            finished+=1
            for nei in adj_list[node]:
                indegree[nei]-=1
                if(indegree[nei]==0):
                    q.append(nei)            
        if finished==numCourses:
            return True
        return False