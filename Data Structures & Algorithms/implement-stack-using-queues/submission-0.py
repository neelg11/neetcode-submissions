from collections import deque
class MyStack:

    def __init__(self):
        self.arr1=deque([])
        self.arr2=deque([])

    def push(self, x: int) -> None:
        while(len(self.arr1)>0):
            tmp=self.arr1.popleft()
            self.arr2.append(tmp)
        self.arr1.append(x)
        while(len(self.arr2)>0):
            tmp=self.arr2.popleft()
            self.arr1.append(tmp)
        print(self.arr1)

    def pop(self) -> int:
        return self.arr1.popleft()

    def top(self) -> int:
        return self.arr1[0]

    def empty(self) -> bool:
        if len(self.arr1)>0:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()