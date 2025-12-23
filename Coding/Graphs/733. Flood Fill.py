class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_c = image[sr][sc]

        def dfs(i,j):
            image[i][j] = color
            nbr = [[0,1],[0,-1],[1,0],[-1,0]]
            for k in nbr:
                if i+k[0]>=0 and i+k[0]<len(image) and j+k[1]>=0 and j+k[1]<len(image[0]):
                    if image[i+k[0]][j+k[1]] == s_c:
                        dfs(i+k[0], j+k[1])
            return
        if color == s_c:
            return image
        dfs(sr,sc)
        return image


