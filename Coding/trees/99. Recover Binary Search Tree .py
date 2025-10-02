# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None
        self.helper(root)
        if self.first and self.second:
            temp = self.first.val
            self.first.val = self.second.val
            self.second.val = temp

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.prev != None and self.prev.val > root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.helper(root.right)
            

    
        