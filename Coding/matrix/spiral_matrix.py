"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

"""

# solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, cols
        t, b = 0, rows
        while l<r and t<b:
            # get top row elements
            for j in range(l,r):
                res.append(matrix[t][j])
            t += 1

            # get right column elements
            for j in range(t,b):
                res.append(matrix[j][r-1])
            r-=1
            if not (l<r and t<b):
                break
            # get bottom row elements
            for j in range(r-1,l-1,-1):
                res.append(matrix[b-1][j])
            b-=1

            # get left column elements
            for j in range(b-1,t-1,-1):
                res.append(matrix[j][l])
            l+=1
        return res

