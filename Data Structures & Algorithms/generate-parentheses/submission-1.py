class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        opened = 0
        closed = 0

        def dfs(opened, closed, curr):
            if opened > n or closed > n:
                return
            if opened == n and closed == n:
                output.append(curr)

            dfs(opened + 1, closed, curr + "(")

            if closed < opened:
                dfs(opened, closed + 1, curr + ")")

        dfs(0, 0, "")
        return output


