# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        def new_func(node,current):
            if not node.left and not node.right:
                result.append("".join(current+[str(node.val)]))
            
            if node.left:
                new_func(node.left,current+[str(node.val)])
            if node.right:
                new_func(node.right,current+[str(node.val)])
        new_func(root,[])
        
        return sum(int(x) for x in result)
                