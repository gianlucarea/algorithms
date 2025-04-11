# 1. Two Sum

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.
from typing import List
import unittest

# This solution finds two numbers in nums that sum to target using a hash map for O(1) lookups. 
# Time: O(n), Space: O(n). 
# Early exit on match.
def twoSum(nums: List[int], target: int) -> List[int]:
    numbers = {}
    for i,n in enumerate(nums):
        difference = target - n
        if difference in numbers:
            return [numbers[difference],i]
        numbers[n] = i

class TestMyFunctions(unittest.TestCase):
    def test_twoSum1(self):
        self.assertEqual(twoSum([2,7,11,15],9), [0,1])
    def test_twoSum2(self):
        self.assertEqual(twoSum([3,2,4],6), [1,2])
    def test_twoSum3(self):
        self.assertEqual(twoSum([3,3],6), [0,1])

if __name__ == '__main__':
    unittest.main()