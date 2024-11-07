#27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        solution = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[solution] = nums[i]
                solution += 1
        return solution
            
