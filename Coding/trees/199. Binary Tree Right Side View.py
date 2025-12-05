# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        # level order
        q = deque()
        q.append(root)
        l = []
        # l.append(root.val)
        # i = 1
        while(q):
            size = len(q)
            # print("level: ", i)
            while(size>0):
                last_poped = q.popleft()
                # print(last_poped.val)
                if last_poped.left:
                    q.append(last_poped.left)
                if last_poped.right:
                    q.append(last_poped.right)
                size -= 1
            # i = i+1
            l.append(last_poped.val)
            # print(l)

        
        return l




            

        