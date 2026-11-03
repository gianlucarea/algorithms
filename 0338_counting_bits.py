# 338. Counting Bits

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i]
# is the number of 1's in the binary representation of i.
# Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).

class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        while len(ans) < n + 1:
            ans += [x + 1 for x in ans]      # prepend a 1-bit to every number so far
        return ans[:n + 1]
