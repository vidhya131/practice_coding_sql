# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.results = []
        self.targetSum = targetSum
        self.dfs(root, 0, [])
        return self.results


    def dfs(self, root, pathsum, patharray):
        # print(root.val)
        pathsum += root.val
        patharray.append(root.val)
        if root and root.left is None and root.right is None:
            # print(pathsum, self.targetSum)
            if pathsum == self.targetSum:
                # print(pathsum, self.targetSum)
                # print(patharray)
                self.results.append(patharray.copy())
                patharray.pop()
                return 
                
        if root.left:
            self.dfs(root.left, pathsum, patharray)
        if root.right:
            self.dfs(root.right, pathsum, patharray)
        patharray.pop()
        