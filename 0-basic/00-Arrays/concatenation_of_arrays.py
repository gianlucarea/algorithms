# 1929. Concatenation of Array

class Solution(object):
    def getConcatenation(self, nums):
       answer = []
       
       for i in range(2):
         for n in nums:
            answer.append(n)
    
       return answer


#Super easy solution! 
# class Solution(object):
#    def getConcatenation(self, nums):
#       return nums + nums
