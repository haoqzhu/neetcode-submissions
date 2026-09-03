# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # create dummy node to return
        left, right = dummy, head   # create left and right to form window

        while n:                    # expand window based on n
            right = right.next
            n -= 1
        
        while right:                # iterate through LL until right hits the end
            left = left.next        # left would be right before node to remove
            right = right.next

        left.next = left.next.next  # set left's next to skip over the node
        return dummy.next           # return