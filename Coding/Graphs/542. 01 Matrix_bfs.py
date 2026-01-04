class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        q = deque()
        drn = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')

        while q:
            poped = q.popleft()
            for i in drn:
                nr = i[0]+poped[0]
                nc = i[1]+poped[1]
                if nr<r and nc<c and nr>=0 and nc>=0:
                    if mat[poped[0]][poped[1]]+1 < mat[nr][nc]:
                        mat[nr][nc] = mat[poped[0]][poped[1]]+1
                        q.append((nr,nc))
        return mat

                   
                    



                
        