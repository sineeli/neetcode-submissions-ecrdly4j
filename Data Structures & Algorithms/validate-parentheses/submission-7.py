class Solution:
    def isValid(self, s: str) -> bool:
        stck = []

        for bracket in s:
            if bracket == "{":
                stck.append(bracket)
            elif bracket == "[":
                stck.append(bracket)
            elif bracket == "(":
                stck.append(bracket)
            if bracket == "}":
                if stck and stck[-1] == "{":
                    stck.pop()
                else:
                    return False
            if bracket == "]":
                if stck and stck[-1] == "[":
                    stck.pop()
                else:
                    return False
            if bracket == ")":
                if stck and stck[-1] == "(":
                    stck.pop()
                else:
                    return False
        
        if stck:
            return False
        
        return True