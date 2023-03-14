# https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/915135563/
# Date of Submission: 2023-03-14

# Runtime: 45 ms, faster than 93.34% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.3MB, less than 9.8% of Python3 online submissions for N-ary Tree Preorder Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        if root is None: 
            return
        
        output.append(root.val)
        
        for child in root.children:
            self.traverse(child, output)