# https://leetcode.com/problems/validate-binary-search-tree/submissions/916938741/
# Date of Submission: 2023-03-17

# Runtime: 43 ms, faster than 81.21% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 71.77% of Python3 online submissions for Validate Binary Search Tree.
#
# Problem:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []
        if root is None:
            return True

        # Since we check left vals first, this needs to be smaller than the smallest value possible
        prevNode = float('-inf')

        while root or path:
            while root:  # DFS to left-lowest node
                path.append(root)
                root = root.left
            root = path.pop()
            if root.val <= prevNode:
                return False
            prevNode = root.val
            root = root.right  # deviate right only if left + middle already checked or in queue

        return True
