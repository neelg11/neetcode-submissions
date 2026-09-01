class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        left,right=0,n-1
        curr_weight,boat=0,0
        while(left<=right):
            if(people[left]+people[right]<=limit):
                left+=1
            boat+=1
            right-=1
        return boat


