# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = None
        return self.inorder_traversal(root)
            

    def inorder_traversal(self, root):
        if not root: 
            return True
        if not self.inorder_traversal(root.left):
            return False
        if self.pre is not None and self.pre.val >= root.val:
            return False
        self.pre = root
        return self.inorder_traversal(root.right)

        
    

        
        

        