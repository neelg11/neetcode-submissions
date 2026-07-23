from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d = defaultdict(list)
        for i in strs:
            freq_map=[0]*26
            for j in i:
                freq_map[ord(j)-ord('a')]+=1
            t=tuple(freq_map)
            d[t].append(i)
        return list(d.values())