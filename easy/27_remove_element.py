# 27. Remove Element
# Removes all occurrences of val in nums in-place and 
# returns the length of the new list without the val.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for j in range(len(nums)):
            if(nums[j] != val):
                nums[k] = nums[j]
                k = k + 1
        return k