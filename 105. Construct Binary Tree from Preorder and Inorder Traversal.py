Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idxmap = defaultdict(int)
        
        for i, n in enumerate(inorder):
            idxmap[n] = i
        
        return self.helper(preorder[::-1], inorder, 0, len(inorder), idxmap)
    
    def helper(self, preorder, inorder, leftPointer, rightPointer, idxmap):
        if leftPointer < rightPointer:
            num = preorder.pop()
            root = TreeNode(num)
            idx = idxmap.get(num)
            
            root.left = self.helper(preorder, inorder, leftPointer, idx, idxmap)
            root.right = self.helper(preorder, inorder, idx + 1, rightPointer, idxmap)
            
            return root
 
