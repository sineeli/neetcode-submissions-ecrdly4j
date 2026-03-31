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

        
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.merge_two(l1, l2))
            
            lists = mergedList
        
        return lists[0]

            



