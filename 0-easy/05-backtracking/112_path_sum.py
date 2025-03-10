# 112. Path Sum
# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all
# the values along the path equals targetSum.
# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathSum(root,targetSum,0)
    
    def pathSum(self,root: Optional[TreeNode],targetSum : int, value: int)->bool:
        if not root: 
            return False
        value += root.val
        if not root.left and not root.right and value == targetSum :
            return True
        if self.pathSum(root.left,targetSum,value):
            return True
        if self.pathSum(root.right,targetSum,value):
            return True
        value -= root.val
        return False
