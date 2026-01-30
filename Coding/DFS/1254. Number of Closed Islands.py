class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        nbr = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            grid[i][j] = 1
            for k in range(1, len(nbr)):
                r = nbr[k-1]+i
                c = nbr[k]+j
                if 0 <= r < rows and  0 <= c <cols and grid[r][c] == 0:
                    dfs(r,c)
        
        for i in range(rows):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][cols-1] == 0:
                dfs(i, cols-1)
        
        for i in range(cols):
            if grid[0][i] == 0:
                dfs(0, i)
            if grid[rows-1][i] == 0:
                dfs(rows-1, i)
        c = 0
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    c += 1
        return c


        


                    

                
                
                



                
