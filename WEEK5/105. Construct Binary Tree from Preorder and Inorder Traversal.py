class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not len(inorder):
            return None
        
        root_val = preorder.pop(0)
        root_index = inorder.index(root_val)

        left_subtree = self.buildTree(preorder, inorder[:root_index])
        right_subtree = self.buildTree(preorder, inorder[root_index+1:])

        root = TreeNode(root_val, left_subtree, right_subtree)

        return root  
        