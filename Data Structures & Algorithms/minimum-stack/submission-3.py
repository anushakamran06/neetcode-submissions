class MinStack:

    def __init__(self):
        self.data = []
    def push(self, val: int) -> None:
        return self.data.append(val)
        
    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.data)








