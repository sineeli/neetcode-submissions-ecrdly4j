# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head

        ll_len = 0
        
        while temp:
            ll_len += 1
            temp = temp.next
        
        temp = head
        if ll_len - n == 0:
            return head.next

        for _ in range(ll_len - n - 1):
            temp = temp.next
        
        if temp.next:
            temp.next = temp.next.next
        
        return head
