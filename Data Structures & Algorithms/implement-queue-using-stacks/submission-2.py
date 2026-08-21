class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not (self.stack2):
            while(self.stack1):
                tmp=self.stack1.pop()
                self.stack2.append(tmp)
        
        return self.stack2.pop()
        
    def peek(self) -> int:
        if not (self.stack2):
            while(self.stack1):
                tmp=self.stack1.pop()
                self.stack2.append(tmp)
        
        return self.stack2[-1]
    def empty(self) -> bool:
        print(self.stack1)
        print(self.stack2)
        return not (bool(len(self.stack1) or len(self.stack2)))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()