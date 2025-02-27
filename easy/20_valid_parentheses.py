#20. Valid Parenthes
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

#Valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
# 3.Every close bracket has a corresponding open bracket of the same type.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_p = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s: 
            if c in map_p:
                stack.append(c)
            elif len(stack) == 0 or map_p[stack.pop()] != c:
                return False
        return len(stack) == 0