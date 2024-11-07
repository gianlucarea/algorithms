# 26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        left = 1
        for right in range(1,len(nums)):
            if(nums[right-1] != nums[right]):
                nums[left] = nums[right]
                left += 1
        return left