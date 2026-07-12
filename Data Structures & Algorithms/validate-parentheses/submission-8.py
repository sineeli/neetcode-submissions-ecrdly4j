class Solution:
    def isValid(self, s: str) -> bool:
        stck = []

        for bracket in s:
            if bracket == "{" or bracket == "[" or bracket == "(":
                stck.append(bracket) 
            elif stck:
                if bracket == "}" and stck[-1] == "{":
                    stck.pop()
                elif bracket == "]" and stck[-1] == "[":
                    stck.pop()
                elif bracket == ")" and stck[-1] == "(":
                    stck.pop()
                else:
                    return False
            else:
                return False
        
        if stck:
            return False
        
        return True