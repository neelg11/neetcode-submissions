class ListNode:
    def __init__(self, val=-1, right=None):
        self.next=right
        self.val=val
class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.size=0
        self.left=ListNode(-1)
        self.right=self.left

    def enQueue(self, value: int) -> bool:
        if(self.size==self.k):
            return False
        else:
            self.right.next=ListNode(value)
            self.size+=1
            self.right=self.right.next
            return True

    def deQueue(self) -> bool:
        if(self.size>0):
            self.left.next=self.left.next.next
            self.size-=1
            if(self.size==0):
                self.right=self.left
            return True
        return False

    def Front(self) -> int:
        if(self.left.next):
            return self.left.next.val
        return -1

    def Rear(self) -> int:
            return self.right.val

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()