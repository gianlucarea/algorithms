# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

import unittest

#This solution finds the longest substring without repeating characters using a sliding window and a set. 
# Time: O(n), Space: O(min(m, n)) (m = character set size). Efficiently tracks unique characters.
def lengthOfLongestSubstring(s: str) -> int:
    string = list(s)
    left = 0
    right = 0
    solution = 0
    substring = set()
    while right < len(string):
        if string[right] not in substring:
            substring.add(string[right])
            solution = max(solution, len(substring))
            right += 1
        else:
            substring.remove(string[left])
            left += 1
    return solution

        
class TestMyFunctions(unittest.TestCase):
    def test_lengthOfLongestSubstring1(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
    def test_lengthOfLongestSubstring2(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
    def test_lengthOfLongestSubstring3(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)
    def test_lengthOfLongestSubstring4(self):
        self.assertEqual(lengthOfLongestSubstring("aab"), 2)
    def test_lengthOfLongestSubstring5(self):
        self.assertEqual(lengthOfLongestSubstring("dvdf"), 3)
if __name__ == '__main__':
    unittest.main()
