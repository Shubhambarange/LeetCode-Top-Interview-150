Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def lenOfLinkedList(self,head):
            length = 0
            temp = head
            while temp != None:
                temp = temp.next
                length += 1
            return length

    def reversKGroup(self,head, k, length):
        # Base Case
        if length < k : return head

        count = 0
        prev = None
        next = None
        curr = head
        # reverse a LL
        while count < k and curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count+=1
        #  Recursive Call
        if next != None: head.next = self.reversKGroup(next, k, length - k)
        return prev 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.lenOfLinkedList(head)
        return self.reversKGroup(head, k, length)

        
