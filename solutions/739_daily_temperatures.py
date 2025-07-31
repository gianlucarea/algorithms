# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after 
# the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

#First solution - Brute force - 
# Time Complexity: O(n) - Space Complexity: O(n)

#def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#    solution : List[int] = [0] * len(temperatures)
#    for i in range(0,len(temperatures)):
#        for j in range(i + 1,len(temperatures)):
#            if temperatures[j] > temperatures[i]:
#                solution[i] = j - i
#                break
#    return solution 

from typing import List
import unittest

# Efficient monotonic stack solution tracks unresolved days, updating results when warmer temperatures are found
# Time Complexity: O(n) - Space Complexity: O(n)
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer : List[int] = [0] * len(temperatures)
    stack = []
    for i , temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)
    return answer

class TestMyFunctions(unittest.TestCase):
    def test_dailyTemperatures1(self):
        self.assertEqual(dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    def test_dailyTemperatures2(self):
        self.assertEqual(dailyTemperatures([30,40,50,60]), [1,1,1,0])
    def test_dailyTemperatures3(self):
        self.assertEqual(dailyTemperatures([30,60,90]), [1,1,0])

if __name__ == '__main__':
    unittest.main()