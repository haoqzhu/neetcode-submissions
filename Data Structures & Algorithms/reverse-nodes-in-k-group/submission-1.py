# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, tail):
        prev, curr = tail, head

        while curr != tail:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = prev = ListNode(0, head)
        
        while True:
            tail = prev
            count = k

            while count and tail:
                tail = tail.next
                count -= 1

            if not tail:
                break
            
            nextGroup = tail.next
            groupHead = prev.next

            prev.next = self.reverse(groupHead, nextGroup)

            prev = groupHead
        
        return res.next
