class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map=[0]*26
        t_map=[0]*26
        n,m=len(s),len(t)
        if n!=m: return False
        for i in range(n):
            s_map[ord(s[i])-ord('a')]+=1
            t_map[ord(t[i])-ord('a')]+=1
        return s_map==t_map
