# 169. Majority Element
#
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = Counter(nums)
        for c in counter:
            if counter[c] > (len(nums) // 2):
                return c
        return -1
