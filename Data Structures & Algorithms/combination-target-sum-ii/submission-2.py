class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subset,ans=[],[]
        sum=0
        n=len(candidates)
        def dfs(i):
            nonlocal sum
            if(target==sum):
                ans.append(subset.copy())
                return
            if(sum>target or i>=n):
                return
            
            subset.append(candidates[i])
            sum+=candidates[i]
            dfs(i+1)
            sum-=candidates[i]
            subset.pop()

            while(i+1<n and candidates[i]==candidates[i+1]):
                i+=1
            dfs(i+1)
        dfs(0)
        return ans


