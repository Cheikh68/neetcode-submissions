class MinStack:
    def __init__(self):
        self.stack = []
        self.preMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.preMin) == 0:
            self.preMin.append(val)
        else:
            self.preMin.append(min(val, self.preMin[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.preMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.preMin[-1]