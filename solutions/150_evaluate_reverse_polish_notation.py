# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

from typing import List
import unittest


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            second,first = stack.pop(), stack.pop()
            stack.append(first - second)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            second,first = stack.pop(), stack.pop()
            stack.append(int(first / second))
        else:
            stack.append(int(c))
    
    return stack[0]

class TestMyFunctions(unittest.TestCase):
    def test_evalRPN1(self):
        self.assertEqual(evalRPN(["2","1","+","3","*"]), 9)
    def test_evalRPN2(self):
        self.assertEqual(evalRPN(["4","13","5","/","+"]), 6)
    def test_evalRPN3(self):
        self.assertEqual(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
    def test_evalRPN4(self):
        self.assertEqual(evalRPN(["-74","-107","-159","-181","/","-56","/","52","+","140","*","-138","+","*","-157","*","-39","+","/"]), 0)
if __name__ == '__main__':
    unittest.main()