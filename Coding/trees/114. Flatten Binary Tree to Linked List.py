# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        q = deque()
        self.preorder(root)
        
    def preorder(self, root , q):
        if root is not None:
            q.append(root)
            self.preorder(root.left, q)
            self.preorder(root.right, q)



        

        