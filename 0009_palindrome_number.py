# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        left, right = 0, len(val)-1
        while left < right:
            if val[left] != val[right]:
                return False
            left += 1
            right -= 1
        return True
