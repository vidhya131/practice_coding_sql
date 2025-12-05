# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.dfs(root, "")
        return self.res
    def dfs(self, root, path):
        if root:
            path = path+"->"+str(root.val)
        if root.left is None and root.right is None:
            path = path[2:]
            self.res.append(path)
            return
        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)

        

        