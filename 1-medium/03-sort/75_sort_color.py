#75. Sort Colors

#Given an array nums with n objects colored red, white, or blue, 
#sort them in-place so that objects of the same color are adjacent, 
#with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in range (0,len(nums)):
            count[nums[i]] += 1

        j = 0
        for n in range(0,len(count)):
            for _ in range(0,count[n]):
                nums[j] = n
                j += 1