# 374. Guess Number Higher or Lower

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1 
        right = n 
        while left <= right:
            middle = (left + right) // 2
            value = guess(middle)
            if value < 0: 
                right = middle - 1
            elif value > 0:
                left = middle + 1
            else:
                return middle