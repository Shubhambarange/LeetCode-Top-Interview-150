
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            
            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels
