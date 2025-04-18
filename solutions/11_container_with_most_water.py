# 11. Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

from typing import List
import unittest

# This solution calculates the maximum water container area using two pointers. 
# Time: O(n), Space: O(1). Efficiently narrows the search by moving the shorter boundary inward.
def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) -1 
    result = 0
    while left < right:
        sx = height[left] 
        dx = height[right]
        h = min(sx, dx)
        b = right - left
        temp = h * b
        result = max(temp,result)
        if sx <= dx: 
            left += 1
        else:
            right -= 1

    return result


class TestMyFunctions(unittest.TestCase):
    def test_maxArea1(self):
        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)
    def test_maxArea2(self):
        self.assertEqual(maxArea([1,1]), 1)

if __name__ == '__main__':
    unittest.main()