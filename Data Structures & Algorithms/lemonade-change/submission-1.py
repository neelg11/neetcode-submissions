class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count=[0]*3
        for i in bills:
            if(i==5):
                count[0]+=1
            elif(i==10):
                count[1]+=1
                if(count[0]==0):
                    return False
                count[0]-=1
            else:
                count[2]+=1
                if(count[1]>0):
                    if(count[0]>0):
                        count[1]-=1
                        count[0]-=1
                    else:
                        return False
                else:
                    if(count[0]>2):
                        count[0]-=3
                    else:
                        return False
        return True
