class MinStack:

    def __init__(self):
        self.stack=[]
        self.length=0
        self.min=float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length+=1

    def pop(self) -> None:
        if self.length>0:
            self.length-=1
            return self.stack.pop()

        

    def top(self) -> int:
        if self.length>0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()