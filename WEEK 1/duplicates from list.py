# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr=head
        while ptr and ptr.next:
            if ptr.next.val==ptr.val:
                ptr.next=ptr.next.next
                continue
            ptr=ptr.next
        return head