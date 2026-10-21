# 104. Maximum Depth of Binary Tree
# A binary tree's maximum depth is the number of nodes along
# the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # The solution i came up first
    def maxDepthBFS(self, root: TreeNode | None) -> int:

        def calculateDepth(node):
            if not node:
                return 1
            left_depth = calculateDepth(node.left)
            right_depth = calculateDepth(node.right)
            return max(left_depth, right_depth) + 1

        return calculateDepth(root) - 1

    # The fastest solution
    def maxDepthDFS(self, root: TreeNode | None) -> int:
        if not root: return 0

        q = deque()
        q.append(root)
        depth = 0
        while q:
            depth += 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth
