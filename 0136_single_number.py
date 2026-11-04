# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        total = 0
        seen = defaultdict(bool)
        for n in nums:
            if n in seen:
                total -= n
            else:
                total += n
                seen[n] = True
        return total
