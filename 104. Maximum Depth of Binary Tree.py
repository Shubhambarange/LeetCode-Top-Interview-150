Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        nodes = deque() # Create a deque to store nodes
        nodes.append(root) # Add the root node to the deque
        levels = 0 # Initialize the depth counter

        while nodes: # Continue traversal while there are nodes in the deque
            levels += 1
            size = len(nodes)

            for i in range(size): # Traverse through the nodes at the current level
                popped_node = nodes.popleft() # Remove the node from the left side of the deque (FIFO)
                if popped_node.left:
                    nodes.append(popped_node.left)  # Add the left child of the current node if it exists
                if popped_node.right:
                    nodes.append(popped_node.right) # Add the right child of the current node if it exists
        return levels  # Return the maximum depth of the binary tree
