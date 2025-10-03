# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = 0 
        r = len(nums)-1
        node = self.constructRoot(nums, l, r)
        return node
        
    def constructRoot(self, nums, l, r):
        if (l>r):
            return None
        print(l,r)
        mid = (l+r)//2
        print(nums[mid])
        root = TreeNode(nums[mid])
        root.left = self.constructRoot(nums, l, mid-1)
        root.right = self.constructRoot(nums, mid+1, r)
        return root

