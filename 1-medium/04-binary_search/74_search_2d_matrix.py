# 74. Search a 2D Matrix

#You are given an m x n integer matrix matrix with the following two properties:
# 1. Each row is sorted in non-decreasing order.
# 2. The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = left + (right - left) // 2
            middle_val = matrix[mid//n][mid%n]
            if target > middle_val:
                left = mid + 1
            elif target < middle_val:
                right = mid - 1
            else:
                return True
        return False

 
