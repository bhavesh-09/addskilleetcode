# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        t
        res = cur = ListNode(0)
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next
        return res.next
        