class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def f(num):
            return abs(num-x)
        ans= (sorted(arr,key=f)[:k])
        return sorted(ans)