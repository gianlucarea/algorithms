# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = strs[0]
        for s in strs[1:]:
            n = min(len(common_prefix),len(s))
            p = 0
            while p < n:
                if common_prefix[p] != s[p]:
                    break
                p += 1
            common_prefix = common_prefix[0:p]
        return common_prefix
