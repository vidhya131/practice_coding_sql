class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0,1):
            return n
        i = 1
        j = 2
        for k in range(3, n+1):
            p = i+j
            i = j
            j = p
        return j
