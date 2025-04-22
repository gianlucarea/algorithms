# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List
import unittest

# This solution calculates trapped rainwater using two pointers and dynamic max tracking. 
# Time: O(n), Space: O(1). Efficiently computes water volume by comparing boundary heights.
def trap(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]    
    water = 0
    while left < right: 
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max,height[right])
            water += right_max - height[right]
    return water   


class TestMyFunctions(unittest.TestCase):
    def test_trap1(self):
        self.assertEqual(trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
    def test_trap2(self):
        self.assertEqual(trap([4,2,0,3,2,5]), 9)

if __name__ == '__main__':
    unittest.main()