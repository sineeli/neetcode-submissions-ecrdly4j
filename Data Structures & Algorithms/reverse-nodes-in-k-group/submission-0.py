# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp_head = head
        temp_tail = head
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        while temp_tail:
            temp_tail = temp_tail.next
            count += 1
            if count == k:
                # After reversing, the old head is now the end of this group
                next_group_start = temp_tail
                prev_tail.next = self.reverse(temp_head, temp_tail)
                
                # Prepare for the next group
                prev_tail = temp_head 
                temp_head = next_group_start
                count = 0
        
        return dummy.next



    
    def reverse(self, head, tail):
        # print(head.val, tail.val)
        temp = head
        prev = tail
        while temp != tail:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        return prev



