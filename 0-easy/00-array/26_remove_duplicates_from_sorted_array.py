# 26. Remove Duplicates from Sorted Array
# Removes duplicates from a sorted list nums in-place and 
# returns the length of the new list without duplicates.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in range(0,len(nums)-1):
            if nums[i] != nums[i + 1]:
                nums[k]=nums[i+1]
                k = k + 1
        return k