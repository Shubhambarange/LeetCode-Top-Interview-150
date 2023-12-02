
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values_tree = {}

        def helper(root, depth):
            if not root: return None
            values_tree[depth] = values_tree.get(depth, []) + [root.val]

            if root.left:
                left = helper(root.left, depth + 1)

            if root.right:
                right = helper(root.right, depth + 1)
        
        helper(root, 0)
        
        return [v if k%2==0 else v[::-1] for k, v in values_tree.items()]
