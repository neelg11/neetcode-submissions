class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        i=0
        for t in tasks:
            t.append(i)
            i+=1
        tasks.sort(key = lambda x:x[0])
        minheap,res=[],[]
        print(tasks)
        i,time=0,tasks[0][0]
        while(i<len(tasks) or minheap):
            while(i<len(tasks) and tasks[i][0]<=time):
                    heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                    i+=1 
            if(not minheap):
                time=tasks[i][0]
            else:
                x=heapq.heappop(minheap)
                time+=x[0]
                res.append(x[1])
                print(x)
        return res

            
