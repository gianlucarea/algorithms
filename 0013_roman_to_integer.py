# 13. Roman to Integer
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        replaceMap = {'IV':'IIII','IX':'VIIII','XL':'XXXX','XC':'LXXXX','CD':'CCCC','CM':'DCCCC'}
        total = 0
        for k,v in replaceMap.items():
            s = s.replace(k,v)

        for ch in s :
            total += symbols[ch]
        return total
