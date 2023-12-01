A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

  Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global massimo

        def ricorri(root: Optional[TreeNode]) -> int:

            global massimo

            if root.left == None and root.right == None:
                if root.val > massimo:
                    massimo = root.val
                return root.val
            
            sx = dx = -9999
            summ = root.val

            if root.left != None:
                sx = ricorri(root.left)

                if sx > 0:
                    summ += sx
                    
            if root.right != None:
                dx = ricorri(root.right)

                if dx > 0:
                    summ += dx                    
            
            if summ > massimo:
                massimo = summ
            
            return root.val + max(dx, sx, 0)
        
        if root == None:
            return None

        massimo = root.val

        if root.left == None and root.right == None:
                return root.val

        sx = dx = None

        summ = root.val

        if root.left != None:
            sx = ricorri(root.left)

            if sx > 0:
                summ += sx
                
        if root.right != None:
            dx = ricorri(root.right)

            if dx > 0:
                summ += dx 
        
        if summ > massimo:
            massimo = summ
        
        return massimo
        
