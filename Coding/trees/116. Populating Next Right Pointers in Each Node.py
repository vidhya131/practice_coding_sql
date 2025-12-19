"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if no elements in tree
        if root is None:
            return root

        # queue for BFS
        q = deque()
        q.append(root)
        while(q):
            size = len(q)
            # visit each node in the same level
            for i in range(size, 1, -1):
                l_poped = q.popleft()
                # connect the current node and next node
                l_poped.next = q[0]
                self.append_2_q(l_poped, q)
            l_poped = q.popleft()
            self.append_2_q(l_poped, q)
        return root

    def append_2_q(self, l_poped, q):
        if l_poped.left:
            q.append(l_poped.left)
        if l_poped.right:
            q.append(l_poped.right)

