# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
from collections import defaultdict
from typing import List
import unittest

# This solution groups anagrams using a hash map with sorted words as keys. 
# Time: O(n * k log k) (k = max word length), Space: O(n * k). Concise and efficient.
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())

class TestMyFunctions(unittest.TestCase):
    def test_groupAnagrams1(self):
        self.assertEqual(groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
    def test_groupAnagrams2(self):
        self.assertEqual(groupAnagrams([""]), [[""]])
    def test_groupAnagrams3(self):
        self.assertEqual(groupAnagrams(["a"]), [["a"]])

if __name__ == '__main__':
    unittest.main()

