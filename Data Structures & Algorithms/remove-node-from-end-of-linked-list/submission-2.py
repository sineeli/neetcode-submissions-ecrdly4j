# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = 0

        temp = head

        if head is None:
            return None

        while temp:
            ll_len += 1
            temp = temp.next
        temp = head

        removeIndex = ll_len - n
        if removeIndex == 0:
            return head.next

        for i in range(ll_len-1):
            if (i + 1) == removeIndex:
                temp.next = temp.next.next
                break
            temp = temp.next
    
        return head
            
        

        