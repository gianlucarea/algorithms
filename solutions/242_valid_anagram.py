# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# This solution checks if two strings are anagrams by comparing character frequencies using a hash map. 
# Time: O(n), Space: O(n). Early termination optimizes it.
from typing import Counter
import unittest

def isAnagram(s: str, t: str) -> bool:
    hm1 = {}
    if len(s) != len(t):
        return False
    for c in s:
        if c in hm1:
            hm1[c] += 1
        else:
            hm1[c] = 1

    for c in t:
        if c not in hm1:
            return False
        if c in hm1:
            hm1[c] -= 1
        if hm1[c] == 0:
            hm1.pop(c)    
    return True

# Optimal Pythonic Solution
# Counter is an unordered collection where elements are stored as Dict keys and their count as dict value.
# So it creates one HashMap for s and one for t and compare it.
def isAnagramOpt( s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

class TestMyFunctions(unittest.TestCase):
    def test_isAnagram1(self):
        self.assertEqual(isAnagram("anagram","nagaram"), True)
    def test_isAnagram2(self):
        self.assertEqual(isAnagram("rat", "car"), False)
    def test_isAnagram3(self):
        self.assertEqual(isAnagram("ab", "a"), False)

if __name__ == '__main__':
    unittest.main()