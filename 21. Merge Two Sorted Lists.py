# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         # Create a sentinel/dummy node to start
        returNode = ListNode(float("-inf"))
         # Create a sentinel/dummy node to start
        headNode = returNode
           # Traverse till one of the lists reaches the end
        while(list1 != None and list2 != None):
            # Compare the values of the two lists
            if list1.val <= list2.val:
                returNode.next = list1
                list1 = list1.next
            else:
                returNode.next  = list2
                list2 = list2.next 
            returNode = returNode.next 
        
         # Append the remaining list
        if (list1 == None):
            returNode.next = list2
        elif list2 == None:
            returNode.next = list1
         # Return the next node to the sentinel node
        return headNode.next
