# BFS, first time we get amount, the depth is ans, dp in visited-> if visited dont explore, level order traversal
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0):
            return 0

        q = deque([amount])
        visited = [False] * (amount+1)
        level = 0
        
        while(q):
            n = len(q)
            level+=1
            for _ in range(n):
                target = q.popleft()
                for coin in coins:
                    if target-coin == 0:
                        return level
                    if(target-coin<0 or visited[target-coin]):
                        continue
                    if target - coin>0:
                        visited[target-coin] = True
                        q.append(target-coin)
        return -1