# 278. First Bad Version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1 
        right = n 
        while left <= right:
            middle = (left + right) // 2
            value = isBadVersion(middle)
            if value == True:
                right = middle - 1
            else:
                left = middle + 1
        return left