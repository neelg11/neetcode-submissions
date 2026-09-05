class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        time_map=[[0]*2 for _ in range(n)]
        for i in range(n):
            time_map[i][0]=position[i]
            time_map[i][1]=(target-position[i])/speed[i]
        time_map=sorted(time_map,key=lambda x:x[0])
        time_map=time_map[::-1]
        # print(time_map)
        prev=-10000000
        ans=n
        for i in time_map:
            if(prev>=i[1]):
                ans-=1
            else:
                prev=i[1]
                
        return ans

