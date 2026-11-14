class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        freq_map = defaultdict(int)
        for edge in trust:
            u, v = edge[0], edge[1]
            freq_map[u]-=1000000
            freq_map[v]+=1
            
        for key,value in freq_map.items():
            if value==n-1:
                return key
        return -1
