# https://leetcode.com/problems/symmetric-tree/submissions/914528408/
# Date of Submission: 2023-03-13

# Runtime: 32 ms, faster than 82.94% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.9 MB, less than 90.34% of Python3 online submissions for Symmetric Tree.
#

# Problem:
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return recurse(root.left, root.right)

def recurse(leftRoot: Optional[TreeNode], rightRoot: Optional[TreeNode]) -> bool:
    if leftRoot is None and rightRoot is None: #return case
        return True
    elif leftRoot is None and rightRoot is not None: #another node exists right but not left
        return False
    elif leftRoot is not None and rightRoot is None: #another node exists left but not right
        return False
    elif leftRoot.val != rightRoot.val: #the values at the nodes are different
        return False
    else: # recurse downwards
        return recurse(leftRoot.left, rightRoot.right) and recurse(leftRoot.right, rightRoot.left)
    