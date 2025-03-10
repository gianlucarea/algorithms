# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder 
# where preorder is the preorder traversal of a binary tree and 
# inorder is the inorder traversal of the same tree,
# construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIndex = inorderIndex = 0
        def dfs(limit):
            nonlocal preorderIndex, inorderIndex
            if preorderIndex >= len(preorder):
                return None
            if inorder[inorderIndex] == limit:
                inorderIndex += 1
                return None
            
            root = TreeNode(preorder[preorderIndex])
            preorderIndex += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))