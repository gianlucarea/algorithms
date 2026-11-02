# 191. Number of 1 Bits

# Given a positive integer n, write a function that returns the number of set bits
# in its binary representation (also known as the Hamming weight).

from collections import Counter

class Solution:
    # My solution was this one
    def hammingWeightPersonalSolution(self, n: int) -> int:
        counter = Counter("{0:b}".format(n))
        return counter['1']

    # Better solution
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
