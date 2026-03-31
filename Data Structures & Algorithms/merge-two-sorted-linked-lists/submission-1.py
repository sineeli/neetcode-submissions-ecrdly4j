# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        dummy = ListNode(-2)
        new = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                dummy.next = h1
                h1 = h1.next
            else:
                dummy.next = h2
                h2 = h2.next

            dummy = dummy.next
        

        while h1:
            dummy.next = h1
            dummy = dummy.next
            h1 = h1.next
        
        while h2:
            dummy.next = h2
            dummy = dummy.next
            h2 = h2.next
        
        return new.next

        