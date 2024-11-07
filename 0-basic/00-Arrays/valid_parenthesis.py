#20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        map_p = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s: 
            if c in map_p:
                stack.append(c)
            elif len(stack) == 0 or map_p[stack.pop()] != c:
                return False
        return len(stack) == 0