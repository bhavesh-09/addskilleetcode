# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q=[root] 
        next_q=[]
        level=[]
        result=[]
        while q!=[]:
            for root in q:
                level.append(root.val)
                if root.left is not None:
                    next_q.append(root.left)
                if root.right is not None:
                    next_q.append(root.right)
            result.append(level)
            level=[]
            q=next_q
            next_q=[]
            
        return result 
        