# 1st Approach:
class MinStack:
    def __init__(self):
        self.stackArr = []

    def push(self, val: int) -> None:
        if not self.stackArr:
            self.stackArr.append([val, val])
            return
        cMin = self.stackArr[-1][1]
        toAdd = min(val, cMin)
        self.stackArr.append([val, toAdd])

    def pop(self) -> None:
        self.stackArr.pop()

    def top(self) -> int:
        return self.stackArr[-1][0]

    def getMin(self) -> int:
        return self.stackArr[-1][1]

# 2nd Approach:
class MinStack:
    def __init__(self):
        self.stackArr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.stackArr.append(val)
        if not self.minArr:
            self.minArr.append(val)
        else:
            self.minArr.append(min(val, self.minArr[-1]))

    def pop(self) -> None:
        self.stackArr.pop()
        self.minArr.pop()

    def top(self) -> int:
        return self.stackArr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
