class MinStack:

    def __init__(self):
        self.stack = []
        self.min_seen = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_seen or val <= self.min_seen[-1]:
            self.min_seen.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_seen[-1]:
            self.min_seen.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_seen[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()