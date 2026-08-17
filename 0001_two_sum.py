# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in diff:
                return [diff[val], i]
            else:
                diff[num] = i
        return [0, 0]
