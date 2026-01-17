class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        drn = [0,1,0,-1,0]

        def dfs(i, j):
            grid[i][j] = 0
            for k in range(4):
                if i+drn[k] < r and i+drn[k] >= 0 and j+drn[k+1] < c and j+drn[k+1] >= 0:
                    if grid[i+drn[k]][j+drn[k+1]] == 1:
                        dfs(i+drn[k], j+drn[k+1])
        
        for i in range(c):
            # boundary
            if grid[0][i] == 1:
                dfs(0,i)
            if grid[r-1][i] == 1:
                dfs(r-1,i)
        
        for i in range(r):
            # boundary
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][c-1] == 1:
                dfs(i,c-1)
        
        # count no of 1's in grid
        count = 0
        for i in grid:
            for j in i:
                if j == 1:
                    count += 1
        return count
    