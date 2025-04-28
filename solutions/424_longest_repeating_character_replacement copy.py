# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.


import unittest

# This solution finds the longest substring with the same character after at 
# most k replacements using a sliding window and frequency map. Time: O(n), Space: O(1)
def characterReplacement(s: str, k: int) -> int:
    left = 0
    frequency = {}
    longest = 0
    for right in range(len(s)):
        if not s[right] in frequency:
            frequency[s[right]] = 0
        frequency[s[right]] += 1
        cells_count = right - left + 1
        if cells_count - max(frequency.values()) <= k:
            longest = max(longest, cells_count)
        else:
            frequency[s[left]] -= 1
            if not frequency[s[left]]:
                frequency.pop(s[left])
            left += 1
    return longest

class TestMyFunctions(unittest.TestCase):
    def test_characterReplacement1(self):
        self.assertEqual(characterReplacement("ABAB",2),4)
    def test_characterReplacement2(self):
        self.assertEqual(characterReplacement("AABABBA",1),4)
    def test_characterReplacement3(self):
        self.assertEqual(characterReplacement("CBAAAABBBBBA",1),6)


if __name__ == '__main__':
    unittest.main()