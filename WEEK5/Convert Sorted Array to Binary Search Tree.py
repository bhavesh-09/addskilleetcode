# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        m=len(nums)//2
        print(m)
        node=TreeNode(nums[m])
        node.left=self.sortedArrayToBST(nums[:m])
        node.right=self.sortedArrayToBST(nums[m+1:])
        return node 
        