#230. Kth Smallest Element in a BST

#Given the root of a binary search tree, and an integer k, 
#return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [] 
        self.inorder(root,result)
        return result[k-1]
        
    def inorder(self, root: Optional[TreeNode],result: List[int]):
        if not root: return
        self.inorder(root.left,result)
        result.append(root.val)
        self.inorder(root.right,result)
        