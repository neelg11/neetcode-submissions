class MinStack:

    def __init__(self):
        self.normalstack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.normalstack.append(val)
        if(len(self.minstack)):
            self.minstack.append(min(val,self.minstack[-1]))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.normalstack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.normalstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

