Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        # Dictionary to map original nodes to their copies
        oldToCopy = {None: None}  # Initialize with None: None mapping

        cur = head
        # First pass: Create copies of nodes without setting next and random pointers
        while cur is not None:
            copy = Node(cur.val)  # Create a copy of the current node
            oldToCopy[cur] = copy  # Map original node to its copy
            cur = cur.next  # Move to the next node in the original list

        cur = head
        # Second pass: Assign next and random pointers for each copied node
        while cur is not None:
            copy = oldToCopy[cur]  # Get the copied node corresponding to current original node
            copy.next = oldToCopy[cur.next]  # Set the 'next' pointer for the copied node
            copy.random = oldToCopy[cur.random]  # Set the 'random' pointer for the copied node
            cur = cur.next  # Move to the next node in the original list

        return oldToCopy[head]  # Return the head node of the copied list
