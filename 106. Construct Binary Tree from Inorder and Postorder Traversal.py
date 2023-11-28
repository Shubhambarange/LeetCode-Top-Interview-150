Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
  
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        hash_map = {}
        for i,n in enumerate(inorder):
            hash_map[n] = i
        self.i = len(postorder) - 1
        def helper(l,r):
            if l > r:
                return None
            root = TreeNode(postorder[self.i])
            mid = hash_map[postorder[self.i]]
            self.i -= 1
            root.right = helper(mid+1,r)

            root.left = helper(l,mid-1)

            return root

        return helper(0,len(postorder) - 1)

        # def helper(l,r):

        #     if l > r:
        #         return None
        #     val = postorder.pop()
        #     root = TreeNode(val)
        #     mid = hash_map[val]
        #     root.right = helper(mid+1,r)
        #     root.left = helper(l,mid-1) 

        #     return root


      
