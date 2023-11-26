Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nodes = deque()
        nodes.append(p)
        nodes.append(q)

        # Loop till the queue is not empty
        while nodes:
            first = nodes.popleft()
            sec = nodes.popleft()

            # check for equality 
            if first == None and sec == None:
                continue 
            elif first == None or sec == None or first.val != sec.val:
                return False

            # add other nodes
            nodes.append(first.left)
            nodes.append(sec.left)
            nodes.append(first.right)
            nodes.append(sec.right)
        
        return True


 
