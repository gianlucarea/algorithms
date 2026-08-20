# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapping = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            mapping[key].append(s)
        return list(mapping.values())
