class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                b = int(stck.pop())
                a = int(stck.pop())
                if token == "+":
                    stck.append(a + b)
                elif token == "-":
                    stck.append(a - b)
                elif token == "*":
                    stck.append(a * b)
                else:
                    stck.append(int(a / b))
            else:
                stck.append(token)
        
        return int(stck[-1])