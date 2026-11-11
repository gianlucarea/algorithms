# 190. Reverse Bits

# Reverse bits of a given 32 bits signed integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        val = bin(n)[::-1]
        val = val[0:len(val)-2]
        if len(val) < 32:
            val = val + ('0' * (32-len(val)))
        return int(val,2)
