class Solution:
    def minEnd(self, n: int, x: int) -> int:
        num, pos = [0]*64, [0]*64
        n=n-1
        last_idx_pos, last_idx_num = 0, 0
        for i in range(64):
            pos[i] = (n>>i) & 1
            num[i] = (x>>i) & 1
            last_idx_pos = i if pos[i] else last_idx_pos
            last_idx_num = i if num[i] else last_idx_num
            
        idx_pos, idx_num = 0, 0
        while(idx_pos <= last_idx_pos):
            if(num[idx_num]==1):
                idx_num+=1
                continue
            num[idx_num]=pos[idx_pos]
            idx_pos+=1
            idx_num+=1
        
        idx, res = 0, 0
        while(idx < last_idx_num+last_idx_pos+3):
            # res+= (num[idx]*(2**idx))
            res+= (num[idx]*(1<<idx))
            idx+=1
        return res