class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m*n
        l = 0
        r = t-1
        while(l<=r and r<t):
            mid = (l+r)//2
            mid_el = self.get(mid, m, n, matrix)
            if  mid_el == target:
                return True
            elif mid_el < target:
                l = mid+1
            else:
                r  = mid-1
        return False

    def get(self, index, rows, cols, matrix):
        ## key logic
        r = index//cols
        c = index%cols
        return matrix[r][c]