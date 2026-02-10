class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        maxi = -1
        for i in range(1,n):
            maxi = max(height[i-1],maxi)
            left_max[i] = maxi
        maxi = -1
        for i in range(n-2, -1, -1):
            maxi = max(height[i+1],maxi)
            right_max[i] = maxi
        
        res = 0
        for i in range(n):
            if height[i]<left_max[i] and height[i]<right_max[i]:
                res += min(left_max[i], right_max[i])-height[i]
        return res

            