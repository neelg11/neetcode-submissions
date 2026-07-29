class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[] for _ in range(len(nums)+1)]
        count_map={}
        for i in nums:
            count_map[i]=count_map.get(i,0)+1
        for key in count_map.keys():
            bucket[count_map[key]].append(key)
        res=[0]*k
        j=0
        for i in reversed(bucket):
            if(j==k):
                break
            if len(i)>0:
                res[j:]=i[:]
                j+=len(i)
        return res

            
            
