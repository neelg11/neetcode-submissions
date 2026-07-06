
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stack=[]
        ans=[]
        while(strs):
            ref=""
            if(len(stack)==0):
                ref=sorted(strs[0])
            for word in strs:
                if(ref==sorted(word)):
                    stack.append(word)
            ans.append(stack.copy())
            while(stack):
                tmp=stack.pop()
                strs.remove(tmp)
        return ans
            