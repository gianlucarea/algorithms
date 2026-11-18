import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        sol = []
        for (x,y) in points:
            dist = -(x*x + y*y)
            if len(sol) == k:
                heapq.heappushpop(sol,(dist,x,y))
            else:
                heapq.heappush(sol,(dist,x,y))


        return [(x,y) for (dist,x, y) in sol]
