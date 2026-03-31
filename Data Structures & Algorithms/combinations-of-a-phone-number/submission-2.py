class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        n: int = len(digits)
        output: list[str] = []
        def dfs(idx: int, res: str):
            if idx == n:
                output.append(res)
                return
            
            for char in digits_map[digits[idx]]:
                dfs(idx + 1, res + char)
        if n == 0:
            return []
        dfs(0, "")
        return output                
