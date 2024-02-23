## SK
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if val < self.mini:
            self.mini = val
        self.stack.append(val)

    def pop(self) -> None:
        p = self.stack.pop()
        if self.stack and p == self.mini:
            self.mini = min(self.stack)
        elif not self.stack:
            self.mini = float('inf')
        return p

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini