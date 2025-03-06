#875 Koko Eating Bananas

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingBanana(mid) -> bool: 
            h_need = 0
            for p in piles:
                h_need += ceil(p/mid)
            return h_need <= h

        left = ceil(sum(piles)/h) 
        right = max(piles)
     
        while left <= right:
            middle = left + (right - left) // 2
            if  eatingBanana(middle):
                right = middle - 1
            else:
                left = middle + 1
        return left