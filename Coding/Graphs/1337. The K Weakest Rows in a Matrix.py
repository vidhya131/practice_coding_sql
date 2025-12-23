class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_sol = len(mat[0])+1
        m = [[] for _ in range(max_sol)]
        for i in range(len(mat)):
            c = 0 
            low, high = 0, max_sol-1
            if mat[i][-1] == 1:
                c = max_sol-1
            else:
                while(low<=high):
                    mid = (low+high)//2
                    if mat[i][mid] == 0:
                        c = mid
                        high = mid-1
                    else:
                        low = mid+1
            m[c].append(i)

        l = []
        for i in range(max_sol):
            for j in m[i]:
                if len(l)<k:
                    l.append(j)
                else:
                    return l
        return l
