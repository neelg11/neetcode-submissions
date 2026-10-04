#CHECK INSIDE and MOVE OUTSIDE
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start = 0
        res_len = 0
        n = len(s)

        #odd center, only 1 char
        for i in range(n):
            l, r = i, i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r-l+1 > res_len:
                    res_start = l
                    res_len = r - l + 1
                l-=1
                r+=1
        #even center, 2 char
        for i in range(n):
            l, r = i, i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r-l+1 > res_len:
                    res_start = l
                    res_len = r - l + 1
                l-=1
                r+=1
        return s[res_start: res_start+res_len]


