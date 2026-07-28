# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        scnd_half = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        scnd_half = slow.next
        slow.next = None

        curr = scnd_half
        scnd_head = None
        while curr:
            temp = curr.next
            curr.next = scnd_head
            scnd_head = curr
            curr = temp

        temp1 = scnd_head
        temp2 = head
        while temp1:
            next_temp2 = temp2.next
            next_temp1 = temp1.next
            
            temp2.next = temp1
            temp1.next = next_temp2
            
            temp2 = next_temp2
            temp1 = next_temp1

        return