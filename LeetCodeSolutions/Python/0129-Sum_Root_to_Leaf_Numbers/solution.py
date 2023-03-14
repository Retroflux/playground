# https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/915021824/
# Date of Submission: 2023-03-14

# Runtime: 28 ms, faster than 88.93% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 13.8 MB, less than 95.89% of Python3 online submissions for Sum Root to Leaf Numbers.
#

# Problem:
#  You are given the root of a binary tree containing digits from 0 to 9 only.
#  Each root-to-leaf path in the tree represents a number.
#  For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
#  Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        
        return(recursiveSum(root.val, root))


def recursiveSum(runningSum, root):
    #short circuit at leaf node - job complete
    if (root.left == None and root.right == None):
        return runningSum

    #else, check left and right for more depth and recurse
    leftSum = 0
    rightSum = 0
    if (root.left != None):
        leftSum = recursiveSum(runningSum*10 + root.left.val, root.left) 
    if (root.right != None):
        rightSum = recursiveSum(runningSum*10 + root.right.val, root.right)
    return leftSum + rightSum