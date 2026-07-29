
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-1)

        temp = dummy

        temp1 = l1
        temp2 = l2
        borrow = 0
        
        while temp1 or temp2 or borrow:
            t1 = temp1.val if temp1 else 0
            t2 = temp2.val if temp2 else 0

            total = t1 + t2 + borrow
            new_node = ListNode(val=total % 10)
            temp.next = new_node
            borrow = total // 10

            if temp1: temp1 = temp1.next
            if temp2: temp2 = temp2.next
            temp = temp.next
        
        return dummy.next