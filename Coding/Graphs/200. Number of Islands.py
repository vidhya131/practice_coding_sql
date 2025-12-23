class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        nbr = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            grid[i][j] = "2"
            for k in nbr:
                if i+k[0]>=0 and i+k[0]<r and j+k[1]>=0 and j+k[1]<c:
                    if grid[i+k[0]][j+k[1]] == "1":
                        dfs(i+k[0], j+k[1])
            return
            
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    # print("island")
                    count += 1
                    dfs(i,j)
        return count



