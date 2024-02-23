#Leo
class MinStack:

    def __init__(self):
        self.storage = []
    def push(self, val: int) -> None:
        min_val = min(val, self.getMin() if self.storage else val)
        self.storage.append((val, min_val))
    def pop(self) -> None:
        return self.storage.pop()

    def top(self) -> int:
        return self.storage[-1][0]

    def getMin(self) -> int:
        return self.storage[-1][1]