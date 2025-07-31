# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

import unittest

# The code checks balanced parentheses using a stack. 
# Time Complexity: O(n) - Space Complexity: O(n)
def isValid(s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0
    
class TestMyFunctions(unittest.TestCase):
    def test_isValid1(self):
        self.assertEqual(isValid("([)]"), False)
    def test_isValid2(self):
        self.assertEqual(isValid("[()([([([([([])])])])])]"), True)
    def test_isValid3(self):
        self.assertEqual(isValid("]"), False)

if __name__ == '__main__':
    unittest.main()