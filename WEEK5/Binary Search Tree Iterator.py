# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.new_Left(root)
        

    def next(self) -> int:
        pointer = self.stack.pop()
        self.new_Left(pointer.right)
        return pointer.val
       
        

    def hasNext(self) -> bool:
        return self.stack
    
    
    def new_Left(self, node):
        while node:
            self.stack.append(node)
            node = node.right
    