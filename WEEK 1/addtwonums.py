# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x,):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=c=ListNode(0)
        carr=0
        while l1 or l2 or carr:
            if l1:
                carr+=l1.val
                l1=l1.next
            if l2:
                carr+=l2.val
                l2=l2.next
            c.next=ListNode(carr%10)
            c=c.next
            carr=carr//10
        return result.next
       