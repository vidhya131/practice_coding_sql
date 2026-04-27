# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = None
        if list1 and list2:
            if list1.val>list2.val:
                sorted_list_head = list2
                list2 = list2.next
            else:
                sorted_list_head = list1
                list1 = list1.next
        elif list1:
            sorted_list_head = list1
            list1 = list1.next
        elif list2:
            sorted_list_head = list2
            list2 = list2.next
        else:
            return sorted_list
        sorted_list = sorted_list_head
        self.merge(list1, list2, sorted_list)
        return sorted_list_head
            
    def merge(self, list1, list2, sorted_list):
        while(list1 and list2):
            if list1.val<list2.val:
                sorted_list.next = list1
                list1 = list1.next
            else:
                sorted_list.next = list2
                list2 = list2.next
            sorted_list = sorted_list.next

        while(list1):
            sorted_list.next = list1
            list1 = list1.next
            sorted_list = sorted_list.next

        while(list2):
            sorted_list.next = list2
            list2 = list2.next
            sorted_list = sorted_list.next