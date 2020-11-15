# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        lh=self.height(root.left)
        rh=self.height(root.right)
        
        ld=self.diameterOfBinaryTree(root.left)
        rd=self.diameterOfBinaryTree(root.right)
        
        return max(lh+rh,max(ld,rd))
    
    def height(self,root):
        if root is None:
            return 0 
        else:
            return 1 + max(self.height(root.left),self.height(root.right)) 