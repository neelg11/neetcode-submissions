class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map=defaultdict(list)
        for s in strs:
            freq_map=[0]*26
            for i in range(len(s)):
                freq_map[ord(s[i])-ord('a')]+=1
            freq_map=tuple(freq_map)
            res_map[freq_map].append(s)
        res=[]
        for value in res_map.values():
            res.append(value)
        return res