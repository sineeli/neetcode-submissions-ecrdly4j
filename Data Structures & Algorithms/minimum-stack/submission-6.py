class MinStack:

    def __init__(self):
        self.stck = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.minstack.append(min(self.minstack[-1] if self.minstack else val, val))
        self.stck.append(val)
        
    def pop(self) -> None:
        self.minstack.pop()
        self.stck.pop()

    def top(self) -> int:
        return self.stck[-1] if self.stck else None

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None
