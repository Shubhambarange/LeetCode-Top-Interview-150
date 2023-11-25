Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
         # Create dummy nodes for values less than x and greater/equal to x
        dummyLess = ListNode(-1)
        before_x = dummyLess

        dummygreter = ListNode(-1)
        after_x = dummygreter

        # Traverse through the original list
        while head:
            if head.val < x:
                 # Attach nodes with values less than x to the 'before_x' list
                before_x.next = head
                before_x = before_x.next

            else:
                 # Attach nodes with values greater/equal to x to the 'after_x' list
                after_x.next = head
                after_x = after_x.next
             # Move to the next node in the original list
            head = head.next
         # Terminate the 'after_x' list
        after_x.next = None
         # Connect the 'before_x' list to the 'after_x' list
        before_x.next = dummygreter.next
     
        # Return the merged list (nodes less than x followed by nodes greater/equal to x)
        return dummyLess.next
