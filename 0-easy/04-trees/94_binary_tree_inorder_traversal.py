#94 Binary Tree Inorder Traversal

#Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root,result)
        return result
    
    def inorder(self, root: Optional[TreeNode], result: List[int]):
        if not root: return
        self.inorder(root.left,result)
        result.append(root.val)
        self.inorder(root.right,result)
        