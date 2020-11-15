# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True 
        return self.isSame(root, root)
            
    def isSame(self,left,right):
        if left == None and right == None:
            return True
        elif left == None or right == None :
            return False 
        else:
            return left.val == right.val and self.isSame(left.left, right.right) and self.isSame(left.right, right.left)