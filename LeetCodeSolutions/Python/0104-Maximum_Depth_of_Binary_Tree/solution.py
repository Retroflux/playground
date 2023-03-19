# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/918243873/
# Date of Submission: 2023-03-19

# Runtime: 33 ms, faster than 97.94% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.2 MB, less than 50.98% of Python3 online submissions for Maximum Depth of Binary Tree.
#
# Problem:
#  Given the root of a binary tree, return its maximum depth.
#  A binary tree's maximum depth is the number of nodes along the longest
#  path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return depthSearch(root, 1)


def depthSearch(root, depth):
    if root.left is None and root.right is None:
        return depth

    leftDepth = 0
    rightDepth = 0
    if root.left is not None:
        leftDepth = depthSearch(root.left, depth+1)
    if root.right is not None:
        rightDepth = depthSearch(root.right, depth+1)
    return max(leftDepth, rightDepth)
