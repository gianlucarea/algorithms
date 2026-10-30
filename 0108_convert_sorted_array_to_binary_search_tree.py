# 108. Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def createTree(input):
            inputLen = len(input)
            if inputLen == 0:
                return None
            if inputLen == 1:
                return TreeNode(input[0])
            mid = inputLen // 2
            root = TreeNode(input[mid])
            root.left = createTree(input[0:mid])
            root.right = createTree(input[mid+1:inputLen])
            return root

        return createTree(nums)
