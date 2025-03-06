# 450. Delete a Node in a Binary Search Tree

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left: return root.right
            elif not root.right: return root.left
            else:
                val = self.findMinInBTS(root.right)
                root.val = val
                root.right = self.deleteNode(root.right,val)
        return root

    def findMinInBTS(self, root: Optional[TreeNode]):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.val