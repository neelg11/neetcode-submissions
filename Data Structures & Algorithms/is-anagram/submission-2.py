class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=[0]*26
        for i in s:
            a[(ord(i)-ord('a'))]+=1
        for i in t:
            a[(ord(i)-ord('a'))]-=1
        for i in a:
            if i!=0: return False
        return True