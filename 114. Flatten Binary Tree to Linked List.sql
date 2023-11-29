Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
  
Example 2:
Input: root = []
Output: []
  
Example 3:

Input: root = [0]
Output: [0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        At each iter 
        left invoc - 
            pass right child if exists
            if no right child, pass arg from prev
        right invoc - 
            pass prev arg
        no right
        """
        if root is None:
            return
        self.flattenHelper(root, None)

    def flattenHelper(self, root: Optional[TreeNode], nextNode: TreeNode) -> None:
        if root is None:
            return
        if root.left:
            if root.right:
                self.flattenHelper(root.left, root.right)
            else:
                self.flattenHelper(root.left, nextNode)
        if root.right:
            if nextNode:
                self.flattenHelper(root.right, nextNode)
            else:
                self.flattenHelper(root.right, None)
                
        if not root.left and not root.right:
            root.right = nextNode
            root.left = None
        else:
            root.right = root.left if root.left else root.right
            root.left = None
