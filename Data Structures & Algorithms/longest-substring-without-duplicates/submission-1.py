class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=ans=0
        charmap={}
        for r in range(len(s)):
            if s[r] in charmap:
                left=max(left,charmap[s[r]]+1)
            charmap[s[r]]=r
            ans=max(ans,r-left+1)
        return ans