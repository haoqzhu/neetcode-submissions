# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next    # Save pointer for the next node to flip
            curr.next = prev    # Set the next to the previous
            prev = curr         # Set the previous to the current
            curr = temp         # Move the pointer to the next node to flip
        return prev