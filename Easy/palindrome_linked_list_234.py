# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        def reverse_linked_list(node):
            prev = None
            current = node

            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        reversed_second_half = reverse_linked_list(slow)

        # Step 3: Compare the first half with the reversed second half
        first_half = head

        while reversed_second_half is not None:
            if first_half.val != reversed_second_half.val:
                return False
            first_half = first_half.next
            reversed_second_half = reversed_second_half.next

        return True
