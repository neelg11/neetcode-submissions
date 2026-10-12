class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if(n!=m): return False
        count_s, count_t = [0]*26, [0]*26
        for i in range(n):
            a, b = ord(s[i]) - ord('a'), ord(t[i])-ord('a')
            count_s[a]+=1
            count_t[b]+=1
        return count_s == count_t