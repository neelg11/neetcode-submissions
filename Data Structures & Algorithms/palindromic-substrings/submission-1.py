#CHECK INSIDE and MOVE OUTSIDE
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(n):
            #odd center, only 1 char
            l, r = i, i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                res+=1
                l-=1
                r+=1
            #even center, 2 char
            l, r = i, i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                res+=1
                l-=1
                r+=1
        return res


