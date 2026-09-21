class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        freq_map=defaultdict(int)
        for list in trust:
            freq_map[list[0]]=-1000000
            freq_map[list[1]]+=1
        for key in freq_map.keys():
            if(freq_map[key]==n-1):
                return key
        return -1