# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

from typing import List
import unittest

# This solution finds all unique triplets in nums that sum to zero using sorting and two pointers. 
# Time: O(n²), Space: O(1) (ignoring output). Efficient and avoids duplicates.

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0: right -= 1
            elif total < 0: left += 1
            else: 
                result.append([nums[i],nums[left],nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return result

class TestMyFunctions(unittest.TestCase):
    def test_threeSum1(self):
        self.assertEqual(threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
    def test_threeSum2(self):
        self.assertEqual(threeSum([0,1,1]), [])
    def test_threeSum3(self):
        self.assertEqual(threeSum([0,0,0]), [[0,0,0]])

if __name__ == '__main__':
    unittest.main()