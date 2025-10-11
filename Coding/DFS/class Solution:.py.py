class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, k, i, j):
            # base cases
            if k==len(word):
                return True
            if i>=len(board) or j>=len(board[i]) or i<0 or j<0 or word[k] != board[i][j]:
                return False
            
            # normal case
            temp = board[i][j]
            board[i][j] = ''
            if dfs(board, word, k+1, i+1, j) or dfs(board, word, k+1, i, j+1) or dfs(board, word, k+1, i-1, j) or dfs(board, word, k+1, i, j-1):
                return True
            
            board[i][j] = temp
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if dfs(board, word, 0, i, j):
                    return True
                
        return False
        