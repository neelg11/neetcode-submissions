class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left=right=ans=0
        n=len(s)
        while(right<n):
            if s[right] not in charset:
                charset.add(s[right])
                right+=1
                ans=max(ans,right-left)
            else:
                charset.remove(s[left])
                left+=1
        return ans
            