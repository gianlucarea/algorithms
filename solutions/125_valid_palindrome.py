# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import unittest

# This solution checks if a string is a palindrome by comparing characters from both ends after
# removing non-alphanumeric characters. Time: O(n), Space: O(n) (due to string cleaning).
def isPalindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class TestMyFunctions(unittest.TestCase):
    def test_isPalindrome1(self):
        self.assertEqual(isPalindrome("A man, a plan, a canal: Panama"), True)
    def test_isPalindrome2(self):
        self.assertEqual(isPalindrome("race a car"), False)
    def test_isPalindrome2(self):
        self.assertEqual(isPalindrome(" "), True)
if __name__ == '__main__':
    unittest.main()