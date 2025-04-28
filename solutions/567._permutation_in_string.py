# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.


from collections import Counter
import unittest

# Checks if any permutation of s1 exists in s2 by comparing 
# frequency counts of sliding windows in s2 with s1's count. 
# Time: O(n * m), Space: O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    h1 = Counter(s1)
    n = len(s1)
    for i in range(len(s2) - len(s1) + 1):
        h2 = Counter(s2[i:i+n])
        if h1 == h2:
            return True
    return False        

class TestMyFunctions(unittest.TestCase):
    def test_checkInclusion1(self):
        self.assertEqual(checkInclusion("ab","eidbaooo"),True)
    def test_checkInclusion2(self):
        self.assertEqual(checkInclusion("ab","eidboaooo"),False)
    def test_checkInclusion3(self):
        self.assertEqual(checkInclusion("a","cccccc"),False)
    def test_checkInclusion4(self):
        self.assertEqual(checkInclusion("abc","cccbcbcbac"),True)


if __name__ == '__main__':
    unittest.main()