class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dynamic programming
        r = len(heights)
        c = len(heights[0])
        pacific = [[False for _ in range(c)] for _ in range(r)]
        atlantic = [[False for _ in range(c)] for _ in range(r)]
         
        def dfs(i, j, visited):
            visited[i][j] = True
            for x,y in [[i-1,j],[i,j-1],[i,j+1],[i+1,j]]:
                if (x >= 0 and x < r and y >= 0 and y < c):
                    if visited[x][y] == False and heights[i][j] <= heights[x][y]:
                        dfs(x, y, visited)
            
        
        for i in range(0, r):
            dfs(i, 0, pacific)
            dfs(i, c-1, atlantic)
        
        for i in range(0, c):
            dfs(0, i, pacific)
            dfs(r-1, i, atlantic)

        result = []
        for i in range(r):
            for j in range(c):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])

        return result
