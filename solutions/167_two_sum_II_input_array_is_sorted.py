# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

from typing import List
import unittest

# My First Solution, Time Complexity O(n) Space Complexity O(1)
# I use two pointers to find the sum and return the solution 
# Time limit exceed for some cases on LeetCode
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left < len(numbers) - 1:
            nLeft = numbers[left]
            right = len(numbers) - 1
            while left < right:
                nRight = numbers[right]
                if ((nLeft + nRight) == target):
                    return [left + 1, right + 1]
                right -= 1
            left += 1

# My Second Solution, Time Complexity O(n) Space Complexity O(1)
# I use two pointers to find the sum and return the solution but in this case I move the pointers using binary search
# as the array is sorted
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        value = numbers[left] + numbers[right]
        if value == target:
            return [left + 1, right + 1]
        if value < target:
            left += 1
        if value > target: 
            right -= 1

class TestMyFunctions(unittest.TestCase):
    def test_twoSum1(self):
        self.assertEqual(twoSum([2,7,11,15],9), [1,2])
    def test_twoSum2(self):
        self.assertEqual(twoSum([2,3,4],6), [1,3])
    def test_twoSum3(self):
        self.assertEqual(twoSum([-1,0], -1), [0,1])

if __name__ == '__main__':
    unittest.main()