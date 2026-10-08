# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = 0
        has_Odd = False
        for v in char_count.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                has_Odd = True

        return length + 1 if has_Odd else length
