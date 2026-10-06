class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = defaultdict(int)
        for i,c in enumerate(s):
            idx_map[c] = i
        ans = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size+=1
            end = max(end, idx_map[c])

            if(i==end):
                ans.append(size)
                size = 0
        return ans
