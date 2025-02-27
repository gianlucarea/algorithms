# 1929. Concatenation of Array
# Given an integer array nums of length n, 
# you want to create an array ans of length 2n 
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return nums + nums Super Easy Solution

        # Reason solution
        n = len(nums)
        answer = [0] * (2 * n)  
        
    
        for i in range(n):
            answer[i] = nums[i]          
            answer[i + n] = nums[i]   
        
        return answer