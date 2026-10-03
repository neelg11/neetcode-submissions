#BFS
class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([n])
        level = 0
        while(q):
            q_size = len(q)
            level+=1
            for itr in range(q_size):
                target = q.popleft()
                for i in range(target+1):
                    if  target - i*i == 0:
                        return level
                    if target < i*i:
                        break
                    q.append(target - i*i)
        return n
