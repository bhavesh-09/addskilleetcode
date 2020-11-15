#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int: 
        
        def new_func(root):
            if root is None:
                return [] 
            nw_left = new_func(root.left)
            root_val = [root.val]
            nw_right = new_func(root.right)
            return nw_left + root_val + nw_right
        
        return new_func(root)[k-1] 
        
