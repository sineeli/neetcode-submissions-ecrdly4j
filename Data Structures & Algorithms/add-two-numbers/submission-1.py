# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2

        carry = 0
        dummy = ListNode(val=-1)
        temp = dummy
        while temp1 or temp2:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0
            digit = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            temp.next = ListNode(digit)

            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
            temp = temp.next
        
        if carry:
            temp.next = ListNode(carry)
        return dummy.next




