# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/915684953
# Date of Submission: 2023-03-15

# Runtime: 30 ms, faster than 94.47% of Python3 online submissions for Check Completeness of a Binary Tree.
# Memory Usage: 13.9 MB, less than 61.14% of Python3 online submissions for Check Completeness of a Binary Tree.

# Problem:
#  Given the root of a binary tree, determine if it is a complete binary tree.
#  In a complete binary tree, every level, except possibly the last, is completely 
#  filled, and all nodes in the last level are as far left as possible. It can have  
#  between 1 and 2h nodes inclusive at the last level h.


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return False

        queue = [root]
        result = []

        # modified BFS queue to include empty nodes in output
        while queue:
            level = []
            l = len(queue)
            for i in range(l):
                currNode = queue.pop(0)
                if currNode == None:
                    level.append(None)
                    continue
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                else:
                    queue.append(None)
                if currNode.right:
                    queue.append(currNode.right)
                else:
                    queue.append(None)
            result.append(level)

        # ensure full, non-empty rows prior to last one
        for i in range(0, len(result)-2):
            for node in result[i]:
                if node is None:
                    return False
        # ensure all numbers are left-aligned for last row
        leftAligned = 1
        for node in result[-2]:
            if node != None and leftAligned == 0:
                return False
            if node == None:
                leftAligned = 0

        # if it survives all checks for contradiction, it's valid
        return True
