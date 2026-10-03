class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1+sqrt5) / 2
        psi = (1-sqrt5) / 2 # or 1-phi
        #psi = 1-psi
        n+=1 # because one '1' is missing
        return int((phi**n - psi**n) / sqrt5)