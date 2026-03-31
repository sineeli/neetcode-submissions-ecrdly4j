class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[-1])
        for token in tokens:
            if token not in "+/-*":
                stack.append(token)
            else:
                if stack:
                    b = int(stack.pop())
                    a = int(stack.pop())

                    if token == "+":
                        c = a + b
                        stack.append(c)
                    elif token == "-":
                        c = a - b
                        stack.append(c)
                    elif token == "*":
                        c = a * b
                        stack.append(c)
                    else:
                        c = a / b
                        if c > 0:
                            stack.append(math.floor(c))
                        else:
                            stack.append(math.ceil(c))
        # print(stack)
        return stack[-1]