Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
  Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # A helper; initiates lower and upper bound
        return self.__subtree(root, float('-inf'), float('inf'))

    def __subtree(self, root: Optional[TreeNode], minimum: Optional[int], maximum: Optional[int]) -> bool:
        # An empty tree is a BST
        if root is None:
            return True
        
        # root.val must be in this range
        if not (minimum < root.val < maximum):
            return False
        
        # Recurse left and right subtree to update values, just so
        # left subtree values must be strictly less than the current node;
        # right subtree values must be strictly greater than the current node
        return (self.__subtree(root.left, minimum, root.val) and
                self.__subtree(root.right, root.val, maximum))


