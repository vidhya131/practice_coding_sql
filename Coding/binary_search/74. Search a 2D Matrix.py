# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val>list2.val:
                sorted_list_head = list2
                list2 = list2.next
            else:
                sorted_list_head = list1
                list1 = list1.next
        elif list1:
            return list1
        else: # this case if for non-empty list2  or both empty
            return list2

        sorted_list = sorted_list_head
        while(list1 and list2):
            if list1.val<list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next
            sorted_list = sorted_list.next

        sorted_list.next = list1 if list1 else list2
        return sorted_list_head
            
        