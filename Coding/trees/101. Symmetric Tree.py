# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = deque()
        q.append(root)
        while(q):
            size = len(q)
            l = []
            while(size>0):
                last_poped = q.popleft()
                l.append(last_poped)
                if last_poped:
                    q.append(last_poped.left)
                    q.append(last_poped.right)
                size -= 1
            
            i = 0
            j = len(l)-1
            while(i<=j):
                if (l[i] is not None and l[j] is None) ^ (l[i] is None and l[j] is not None):
                    return False
                if l[i] is None and l[j] is None:
                    pass
                elif l[i].val != l[j].val:
                    return False
                i +=1
                j -=1
            
        return True
                    
