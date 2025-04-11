#217. Contains Duplicate

# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.

from typing import List
import unittest

# This solution uses a set to track seen numbers, 
# checking for duplicates in O(n) time and O(n) space. 
# Early termination improves efficiency.
def containsDuplicate(nums: List[int]) -> bool:
        duplicates = set()
        for _, number in enumerate(nums):
            if number in duplicates:
                return True
            duplicates.add(number)
        return False
    
class TestMyFunctions(unittest.TestCase):
    def test_containsDuplicate1(self):
        self.assertEqual(containsDuplicate([1,2,3,1]), True)
    def test_containsDuplicate2(self):
        self.assertEqual(containsDuplicate([1,2,3,4]), False)
    def test_containsDuplicate3(self):
        self.assertEqual(containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
    def test_containsDuplicate4(self):
        self.assertEqual(containsDuplicate([]), False)

if __name__ == '__main__':
    unittest.main()