# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i=1
        while(True):
            mid1=i+(n-i)//3
            mid2=n-(n-i)//3
            dir1=guess(mid1)
            dir2=guess(mid2)
            if(dir1==0): return mid1
            if(dir2==0): return mid2

            if(dir1==-1): n=mid1-1
            elif(dir2==1): i=mid2+1
            else:
                i=mid1+1
                n=mid2-1

