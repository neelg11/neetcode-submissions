class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n , m = len(str1), len(str2)
        smaller = min ( len(str1), len(str2) )
        def gcd_str(l):
            if(n%l or m%l):
                return False
            l1, l2 = n//l, m//l
            if str1[:l]*l2 == str2 and str2[:l]*l1 == str1:
                return True
            return False
        
        for i in range(smaller, 0, -1):
            if(gcd_str(i)):
                return str1[:i]
        return ""
            