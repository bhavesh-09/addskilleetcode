# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def new_func(node):   
            if not node: 
                return 0
            if node.val < low: 
                return new_func(node.right)
            elif node.val > high: 
                return new_func(node.left)
            else: 
                return new_func(node.left) + new_func(node.right) + node.val
        return new_func(root)  
        