# 36. Valid Sudoku
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

from collections import defaultdict
from typing import List
import unittest

# This solution checks Sudoku validity using hash sets for rows, columns, and 3x3 sub-boxes. 
# Time: O(1) (fixed 81 cells), Space: O(1) (fixed storage). Efficient and clear.
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r// 3, c // 3)]:
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            boxes[(r // 3, c // 3)].add(board[r][c])
    return True



class TestMyFunctions(unittest.TestCase):
    def test_isValidSudoku1(self):
        self.assertEqual(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]), True)
    def test_isValidSudoku2(self):
        self.assertEqual(isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]), False)
if __name__ == '__main__':
    unittest.main()