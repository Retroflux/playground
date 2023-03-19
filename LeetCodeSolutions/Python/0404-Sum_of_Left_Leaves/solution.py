# https://leetcode.com/problems/sum-of-left-leaves/submissions/918252663/
# Date of Submission: 2023-03-19

# Runtime: 40 ms, faster than 26.95% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.8 MB, less than 40.61% of Python3 online submissions for Sum of Left Leaves.
#
# Problem:
#  Given the root of a binary tree, return the sum of all left leaves.
#  A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        return recursiveSum(root, "right")


def recursiveSum(root, lastDirection):

    if root.left is None and root.right is None and lastDirection is "left":
        return root.val
    elif root.left is None and root.right is None and lastDirection is "right":
        return 0

    tempSum = 0
    if root.left:
        tempSum += recursiveSum(root.left, "left")
    if root.right:
        tempSum += recursiveSum(root.right, "right")

    return tempSum
