class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_map=[[0]*2 for _ in range(len(position))]
        for i in range(len(position)):
            time_map[i][0]=position[i]
            time_map[i][1]=(target-position[i])/speed[i]
        time_map=sorted(time_map, key=lambda x:x[0])
        time_map=time_map[::-1]
        curr_max_time=-1000000000 
        ans=0
        #ans marks the fleet led by the last position car, curr_max_time marks the time taken by it, if any position before it takes less time, than it merges, else curr_max_time increases
        for i in range(len(position)):
            if(curr_max_time<time_map[i][1]):
                curr_max_time=time_map[i][1]
                ans+=1
        return ans
