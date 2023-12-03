Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        else:
            return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = self.inOrder(root)
        minDiff = res[1] - res[0]
        for i in range(2, len(res)):
            if res[i] - res[i-1] < minDiff:
                minDiff = res[i] - res[i-1]
        return minDiff
