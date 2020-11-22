# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if  not root:
            return True 
        def io(root):
            if root.left:
                io(root.left)
            result.append(root.val)
            if root.right:
                io(root.right)
        result=[]
        io(root)
        if sorted(result)==result and len(set(result))==len(result):
            return True 
        return False


       