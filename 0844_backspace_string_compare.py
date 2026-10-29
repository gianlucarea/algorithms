# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into
# empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def createStack(input: str):
            stack = []
            for ch in input:
                if ch == "#":
                    if len(stack) > 0:
                        stack.pop()
                    continue
                stack.append(ch)
            return stack

        return createStack(s) == createStack(t)
