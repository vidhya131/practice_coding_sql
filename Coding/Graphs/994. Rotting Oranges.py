class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the rotten oranges
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))

        # BFS
        time = 0
        l = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            sze = len(q)
            for i in range(sze):
                poped = q.popleft()
                for j in l:
                    if poped[0]+j[0] >= 0 and poped[0]+j[0] < len(grid) and poped[1]+j[1] >= 0 and poped[1]+j[1] < len(grid[0]):
                        if grid[poped[0]+j[0]][poped[1]+j[1]] == 1:
                            grid[poped[0]+j[0]][poped[1]+j[1]] = 2
                            q.append((poped[0]+j[0], poped[1]+j[1]))
            if len(q)>0:
                time += 1
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return time

                            





        