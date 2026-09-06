class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min=val
        else:
            self.stack.append(val-self.min)
            self.min=min(self.min, val)
    def pop(self) -> None:
        popped=self.stack.pop()
        if(popped<0):
            self.min=self.min-(popped)
            popped=self.min
        else:
            popped=popped+self.min
        print(popped)
            

    def top(self) -> int:
        top_val=self.stack[-1]
        if(top_val>0):
            return top_val+self.min
        return self.min

    def getMin(self) -> int:
        return self.min
