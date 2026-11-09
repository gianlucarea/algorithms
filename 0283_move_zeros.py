# 283. Move Zeroes
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        p = 0
        for n in nums:
            if n != 0:
                nums[p] = n
                p += 1
        for i in range(p, len(nums)):
            nums[i] = 0
