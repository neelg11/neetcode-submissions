#implement stack using one queue at pop side
class MyStack:

    def __init__(self):
        self.q1 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        n = len(self.q1)
        temp = 0
        for _ in range(n-1):
            temp = self.q1.popleft()
            self.q1.append(temp)
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[len(self.q1)-1]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()