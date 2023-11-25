Given the head of a linked list, rotate the list to the right by k places.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge Cases
        if head == None or head.next == None or k == 0: return head

        # Count the length of LL and find the last node
        cur = head
        len_count = 1
        while cur.next:
            len_count += 1
            cur = cur.next

        # Make the linked list circular
        cur.next = head

        # Calculate the actual rotation amount within the length
        k = k % len_count
        k = len_count - k

        # Go till the target node (kth node from the end)
        while k > 0: 
            cur = cur.next
            k-=1
            
          # Set head to the new rotated head and break the circular structure
        head = cur.next
        cur.next = None

        return head



