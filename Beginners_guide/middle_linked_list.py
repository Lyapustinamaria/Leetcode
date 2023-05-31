# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = head
        while new_head and new_head.next:
            
            head = head.next
            new_head = new_head.next.next

        return head