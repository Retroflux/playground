class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p or root.val == q:
            return root

        #get paths, store values as lists
        p_Path = findPath(root, p.val, [root.val])
        q_Path = findPath(root, q.val, [root.val])
        longestPath = []
        shortestPath = []

        matchIndex = 0

        if len(p_Path) >= len(q_Path):
            longestPath = p_Path
            shortestPath = q_Path
        else:
            longestPath = q_Path
            shortestPath = p_Path

        #find depth of LCA
        for i in range(len(longestPath)-1, -1, -1):
            if longestPath[i] in shortestPath:
                matchIndex = i
                break

        # traverse tree using the path we built as a guide until you reach the correct depth
        for i in range(1, matchIndex+1):
            if root.left and root.left.val == longestPath[i]:
                root = root.left
            else:
                root = root.right
        return root

# FYI this would be much more complicated if it wasn't a binary search tree
# we can take a lot of shortcuts because of that. 
def findPath(root, target, currPath):
    while target != currPath[-1]:
        if root.left and target < root.val:
            currPath.append(root.left.val)
            root = root.left
        else:
            currPath.append(root.right.val)
            root = root.right
    return currPath
