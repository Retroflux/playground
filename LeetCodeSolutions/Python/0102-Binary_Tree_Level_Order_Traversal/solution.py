# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/915684953
# Date of Submission: 2023-03-15

# Runtime: 32 ms, faster than 85.92% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.1 MB, less than 98.22% of Python3 online submissions for Binary Tree Level Order Traversal.

# Problem:
#  Given the root of a binary tree, return the level order traversal of its 
#   nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        queue = [root]

        result = []

        while queue:
            level = []
            l = len(queue)
            for i in range(l):
                currNode = queue.pop(0)
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(level)
        return result
