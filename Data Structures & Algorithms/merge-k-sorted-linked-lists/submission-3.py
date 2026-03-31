# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge_two(self, l1: ListNode, l2: ListNode):
        temp1 = l1
        temp2 = l2

        new = ListNode(-1)
        temp3 = new
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
            temp3 = temp3.next
            
        while temp1:
            temp3.next = temp1
            temp1 = temp1.next
            temp3 = temp3.next

        while temp2:
            temp3.next = temp2
            temp2 = temp2.next
            temp3 = temp3.next
        
        return new.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        output = [lists[0]]

        for i in range(1, len(lists)):
            temp = self.merge_two(output[-1], lists[i])
            output.append(temp)
            while temp:
                print(temp.val)
                temp = temp.next

        
        return output[-1]
           
            



