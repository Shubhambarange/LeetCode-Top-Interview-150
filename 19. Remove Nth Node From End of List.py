Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        fristPtr = dummy
        secPtr = dummy.next

        while n>1:
            secPtr = secPtr.next
            n-=1
        
        while secPtr.next != None:
             fristPtr = fristPtr.next
             secPtr = secPtr.next
            
        fristPtr.next = fristPtr.next.next
    
        return dummy.next
        
