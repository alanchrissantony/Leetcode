class MyStack:

    def __init__(self):
        self.stack=[]
        self.length=0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length+=1
    def pop(self) -> int:
        if self.length>0:
            self.length-=1
            return self.stack.pop()
        return False

    def top(self) -> int:
        if self.length>0:
            return self.stack[-1]
        return False
        
    def empty(self) -> bool:
        return self.length==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()