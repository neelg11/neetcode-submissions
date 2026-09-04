class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)): return False
        map_s1=[0]*26
        map_s2=[0]*26
        l=len(s1)
        for i in range(len(s2)):
            if(i<len(s1)):
                map_s1[ord(s1[i])-ord('a')]+=1
                map_s2[ord(s2[i])-ord('a')]+=1
            else:
                map_s2[ord(s2[i-l])-ord('a')]-=1
                map_s2[ord(s2[i])-ord('a')]+=1
            print(f"{i}: {map_s2}")
            if(i+1>=len(s1)) and map_s1==map_s2:
                    return True
        return False
            

            
