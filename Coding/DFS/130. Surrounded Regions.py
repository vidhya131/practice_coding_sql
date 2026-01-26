class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        nbr = [0,1,0,-1,0]
        def dfs(i,j):
            # connected to border
            board[i][j] = "P"
            for k in range(4):
                u = nbr[k]+i
                v = nbr[k+1]+j
                if 0 <= u < r and 0 <= v < c and board[u][v] == "O":
                    dfs(u,v)
        # start from boarders of board
        for i in range(r):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][c-1] == "O":
                dfs(i,c-1)
        for i in range(c):
            if board[0][i] == "O":
                dfs(0,i)
            if board[r-1][i] == "O":
                dfs(r-1,i)
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "P":
                    board[i][j] = "O"

        