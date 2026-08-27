class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C and board[r][c] == "O"):
                return

            board[r][c] = "#"

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                curr_r, curr_c = r + dr, c + dc
                dfs(curr_r, curr_c)

        for i in range(R):
            dfs(i, 0)
            dfs(i, C - 1)

        for j in range(C):
            dfs(0, j)
            dfs(R - 1, j)

        for i in range(R):
            for j in range(C):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

