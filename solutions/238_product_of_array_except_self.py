# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List
import unittest

# This solution computes the product of all elements except nums[i] 
# in O(n) time and O(1) space (excluding output), using prefix and suffix products.
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    for i in range(1,n):
        result[i] = result[i-1] * nums[i-1]

    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result

class TestMyFunctions(unittest.TestCase):
    def test_productExceptSelf1(self):
        self.assertEqual(productExceptSelf([1,2,3,4]), [24,12,8,6])
    def test_productExceptSelf2(self):
        self.assertEqual(productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])
        
if __name__ == '__main__':
    unittest.main()