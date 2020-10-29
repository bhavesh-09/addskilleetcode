# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        # step 1: store the values of the linked list into a list and sort the list
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        # step 2: use the sorted list to build the new linked list
        res = cur = ListNode(0)
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next
        return res.next
        