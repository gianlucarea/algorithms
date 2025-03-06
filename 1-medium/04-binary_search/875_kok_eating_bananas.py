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