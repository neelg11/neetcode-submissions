class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        j=len(asteroids)-1
        while(j>=0):
            #collapse happens only when top is negative and new num is positive
            if(stack and stack[-1]<0 and asteroids[j]>0):
                #collapse 3 ways, 1. equal weight, just pop||| 2. negative more, do nothing ||| 
                #3. positve more, keep poping until negative is bigger, equal or gone so 3 again has 3 points.

                #1 Collapse one: Equal Weights, both dies, so only one pop
                if(stack[-1]+asteroids[j]==0): 
                    stack.pop()
                    j-=1
                #2 Collapse two: Negative is bigger, only positive dies, do nothing
                elif(stack[-1]+asteroids[j]<0): 
                    j-=1
                #3 Collapse three, negative dies, positive survive, and might keep more negative, or might die itself later
                else:
                    stack.pop()
                    # so i popped, and did not move j back, so it will go in while loop again and see all conditions again
            else:
                stack.append(asteroids[j])
                j-=1
        ans=stack[::-1]
        return ans

                
