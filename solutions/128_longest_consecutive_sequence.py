# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

from typing import List
import unittest

# My first solution 
# runs in O(n) but gives Time Limited Exception in Leetcode for some cases
# I just transform the array in hashmap and then for each number in array I check if there is a sequence by looking at the
# key of the hashtable
def longestConsecutiveWithHashMap(nums: List[int]) -> int:
    hashmap = {k: k for k in nums} 
    result = 0
    for _,number in enumerate(nums):
        temp_result = 1
        temp = number + 1
        while temp in hashmap: 
                temp_result += 1
                temp += 1
        result = max(result,temp_result)
    return result

# My second solution 
# runs in O(n) I use a hashset instead of an hashmap as i need just the key and not the key,value property 
# I also check if number - 1 is not in the set to avoid calculate not necessary sequence
def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    result = 0
    for number in nums_set:
        if number - 1 not in nums_set:
            temp_result = 1
            temp = number
            while temp + 1 in nums_set:
                temp_result += 1            
                temp += 1
            result = max(result,temp_result)
    return result

class TestMyFunctions(unittest.TestCase):
    def test_longestConsecutive1(self):
        self.assertEqual(longestConsecutive([100,4,200,1,3,2]), 4)
    def test_longestConsecutive2(self):
        self.assertEqual(longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
    def test_longestConsecutive3(self):
        self.assertEqual(longestConsecutive([1,0,1,2]), 3)
    def test_longestConsecutive4(self):
        self.assertEqual(longestConsecutive([]), 0)
if __name__ == '__main__':
    unittest.main()