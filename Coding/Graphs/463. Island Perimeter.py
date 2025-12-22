class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def perimeter(i,j):
            return sum(
                1
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]
                if not (0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == 1)
            )

        per = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # check neighbours
                    per += perimeter(i,j)
        return per
    
    


        


        