class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = defaultdict(int)
        for i,c in enumerate(s):
            idx_map[c] = i

        n = len(s)
        ans = []
        l = 0
        while(l<n):
            i = r = l
            while(i<=r):
                r = max(r, idx_map[s[i]])
                i += 1
            # ans.append(i-l)
            ans.append(r-l+1)
            l = i
        return ans
