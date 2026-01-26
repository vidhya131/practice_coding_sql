class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nbr = [0,1,0,-1,0]
        def dfs(i,j):
            grid[i][j] = 0
            c = 1
            for k in range(0, len(nbr)-1):
                p = nbr[k]+i
                q = nbr[k+1]+j
                if p>=0 and p<len(grid) and q>=0 and q<len(grid[0]) and grid[p][q] == 1:
                    c += dfs(p, q)
            return c
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c = dfs(i, j)
                    if res<c:
                        res = c
        return res

