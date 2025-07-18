class MyQueue:

    def __init__(self):
        self.queue=[]
        self.length=0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length+=1

    def pop(self) -> int:
        if self.length>0:
            self.length-=1
            return self.queue.pop(0)
        return False

    def peek(self) -> int:
        if self.length>0:
            return self.queue[0]
        return False   

    def empty(self) -> bool:
        return self.length==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()