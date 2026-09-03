# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1:
            return None
        elif len(lists) == 1:
            return lists[0]

        def mergeLists(list1, list2):
            head = node = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            
            node.next = list1 or list2
            return head.next

        while len(lists) > 1:
            list1 = lists.pop()
            list2 = lists.pop()
            lists.append(mergeLists(list1, list2))

        return lists[0]
