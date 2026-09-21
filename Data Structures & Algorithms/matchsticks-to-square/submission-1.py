class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len=sum(matchsticks)
        if(total_len)%4!=0: return False

        side_len=total_len//4
        bucket=[0]*4

        for size in matchsticks:
            if(size>side_len): return False
        matchsticks.sort(reverse=True)
        def dfs(i):
            nonlocal bucket
            if(i==len(matchsticks)):
                return all(side_len == bucket[i] for i in range(4))
            for s in range(4):
                if bucket[s]+matchsticks[i]>side_len:
                    continue
                bucket[s]+=matchsticks[i]
                if dfs(i+1):
                    return True
                bucket[s]-=matchsticks[i]
            return False
        return dfs(0)

        

