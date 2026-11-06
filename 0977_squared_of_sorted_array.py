# 977. Squares Of A Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the
# squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquaresEasy(self, nums: list[int]) -> list[int]:
        # Easy Solution
        return sorted([nums[i]*nums[i] for i in range(len(nums))])

    def sortedSquaresLinear(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        left , right = 0, len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        return result
