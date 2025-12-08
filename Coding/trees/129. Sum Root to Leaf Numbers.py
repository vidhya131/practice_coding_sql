# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.pathsum = 0
        self.dfs(root, "")
        return self.pathsum
    
    def dfs(self, root, num):
        # print(root.val)
        num += str(root.val)
        if root and root.left is None and root.right is None:
            # print("in end:",num)
            self.pathsum += int(num)
        
        # print(num)
        if root.left:
            self.dfs(root.left, num)
        if root.right:
            self.dfs(root.right, num)
        
        
    


        
        