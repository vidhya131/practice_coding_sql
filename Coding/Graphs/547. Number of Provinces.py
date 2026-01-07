class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r = c = len(isConnected)
        
        vis = [False]*r
        def dfs(i):
            vis[i] = True
            for j in range(r):
                if isConnected[i][j] == 1 and vis[j] == False:
                    dfs(j)
            return

        count = 0
        for i in range(r):
            if vis[i] == False:
                dfs(i)
                count += 1
        return count




                



        

        