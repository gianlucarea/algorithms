# 110. Balanced Binary Tree
#
# Given a binary tree, determine if it is height-balanced.
#
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def checkNode(node):
            if not node: return 0, True
            left_heigth, left_is_balanced = checkNode(node.left)
            right_heigth, right_is_balanced = checkNode(node.right)
            return max(left_heigth, right_heigth) + 1 , left_is_balanced and right_is_balanced and abs(left_heigth - right_heigth) <= 1

        _, balanc = checkNode(root)
        return balanc
