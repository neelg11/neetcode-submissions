class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        num = n
        while(True):
            if num in visited:
                return False
            if num == 1:
                return True
            visited.add(num)
            next_num=0
            while(num):
                next_num+= ((num%10)**2)
                num = num//10
            num = next_num
                