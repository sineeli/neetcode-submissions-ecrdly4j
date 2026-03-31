class MinStack:

    def __init__(self):
        self.st = []
        self.size = 0
        self.min_st = []
        

    def push(self, val: int) -> None:
        if not self.min_st:
            self.min_st.append(val)
        else:
            if val <= self.min_st[-1]:
                self.min_st.append(val)
        self.st.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        if val == self.min_st[-1]:
            self.min_st.pop()
        return
        

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]

        
